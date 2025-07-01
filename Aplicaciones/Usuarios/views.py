from django.shortcuts import render, redirect
from .models import Usuario # Importa tu modelo Usuario
from django.contrib import messages
# Importa PasswordHasher para hashear contraseñas (muy importante)
from django.contrib.auth.hashers import make_password

# --- Vistas de Gestión de Usuarios ---

def inicioU(request):
    listadoUsuarios = Usuario.objects.all()
    return render(request, "inicioU.html", {'usuarios': listadoUsuarios})

def nuevoUsuario(request):
    return render(request, "nuevoUsuario.html")

def guardarUsuario(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]
        cedula = request.POST["cedula"]
        # Es CRUCIAL hashear la contraseña antes de guardarla
        contrasena_plana = request.POST["contrasena"]
        contrasena_hasheada = make_password(contrasena_plana) # Hasheando la contraseña

        try:
            nuevo_usuario = Usuario.objects.create(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                cedula=cedula,
                contrasena=contrasena_hasheada # Guardamos la contraseña hasheada
            )
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect('inicio_usuarios') # Redirige a la vista de inicio de usuarios
        except Exception as e:
            messages.error(request, f"Error al registrar el usuario: {e}")
            return redirect('nuevo_usuario') # Redirige de vuelta al formulario

    messages.error(request, "Método de solicitud no válido.")
    return redirect('inicio_usuarios')


def eliminarUsuario(request, id):
    try:
        usuario_a_eliminar = Usuario.objects.get(id=id)
        usuario_a_eliminar.delete()
        messages.success(request, "Usuario eliminado exitosamente.")
    except Usuario.DoesNotExist:
        messages.error(request, "El usuario no existe.")
    except Exception as e:
        messages.error(request, f"Error al eliminar el usuario: {e}")
    return redirect('inicio_usuarios')


def editarUsuario(request, id):

    try:
        usuario_a_editar = Usuario.objects.get(id=id)
        return render(request, "usuarios/editarUsuario.html", {'usuarioEditar': usuario_a_editar})
    except Usuario.DoesNotExist:
        messages.error(request, "El usuario no existe.")
        return redirect('inicio_usuarios')


def procesarEdicionUsuario(request, id):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(id=id) # Busca el usuario por el ID de la URL
            usuario.nombre = request.POST["nombre"]
            usuario.apellido = request.POST["apellido"]
            usuario.correo = request.POST["correo"]
            usuario.cedula = request.POST["cedula"]
            
            # Solo actualiza la contraseña si se proporciona una nueva
            nueva_contrasena = request.POST.get("contrasena", "").strip()
            if nueva_contrasena: # Si el campo de contraseña no está vacío
                usuario.contrasena = make_password(nueva_contrasena) # Hashea y guarda la nueva contraseña
            
            usuario.save()
            messages.success(request, "Usuario actualizado exitosamente.")
            return redirect('inicio_usuarios')
        except Usuario.DoesNotExist:
            messages.error(request, "El usuario no existe.")
            return redirect('inicio_usuarios')
        except Exception as e:
            messages.error(request, f"Error al actualizar el usuario: {e}")
            # Considera redirigir a la página de edición nuevamente con los datos, o al inicio
            return redirect('editar_usuario', id=id) 
            
    messages.error(request, "Método de solicitud no válido.")
    return redirect('inicio_usuarios')