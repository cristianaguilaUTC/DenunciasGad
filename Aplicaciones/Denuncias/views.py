from django.shortcuts import render, redirect
from .models import Denuncia
from Aplicaciones.Usuarios.models import Usuario
from django.contrib import messages

# Mostrar listado de denuncias
def inicioD(request):
    listadoDenuncias = Denuncia.objects.all()
    return render(request, "inicioD.html", {'denuncias': listadoDenuncias})

# Mostrar formulario nueva denuncia
def nuevaDenuncia(request):
    usuarios = Usuario.objects.all()  # Para seleccionar el usuario en un combo
    return render(request, "nuevaDenuncia.html", {'usuarios': usuarios})

# Guardar denuncia en la base
def guardarDenuncia(request):
    if request.method == 'POST':
        usuario_id = request.POST["usuario"]
        tipo_denuncia = request.POST["tipo_denuncia"]
        descripcion = request.POST["descripcion"]
        latitud = request.POST["latitud"]
        longitud = request.POST["longitud"]
        referencia = request.POST["referencia"]
        estado = request.POST.get("estado", "pendiente")  # Por defecto pendiente

        evidencia = request.FILES.get('evidencia', None)

        try:
            usuario = Usuario.objects.get(id=usuario_id)

            nueva_denuncia = Denuncia.objects.create(
                usuario=usuario,
                tipo_denuncia=tipo_denuncia,
                descripcion=descripcion,
                latitud=latitud,
                longitud=longitud,
                referencia=referencia,
                estado=estado,
                evidencia=evidencia
            )
            messages.success(request, "Denuncia registrada exitosamente.")
            return redirect('/denuncias/')
        except Exception as e:
            messages.error(request, f"Error al guardar la denuncia: {e}")
            return redirect('/denuncias/nuevaDenuncia/')
    else:
        messages.error(request, "Método no permitido.")
        return redirect('/denuncias/')

# Eliminar denuncia
def eliminarDenuncia(request, id):
    try:
        denuncia = Denuncia.objects.get(id=id)
        denuncia.delete()
        messages.success(request, "Denuncia eliminada exitosamente.")
    except Denuncia.DoesNotExist:
        messages.error(request, "La denuncia no existe.")
    return redirect('/denuncias/')

# Mostrar formulario para editar denuncia
def editarDenuncia(request, id):
    try:
        denuncia = Denuncia.objects.get(id=id)
        usuarios = Usuario.objects.all()
        return render(request, "editarDenuncia.html", {'denunciaEditar': denuncia, 'usuarios': usuarios})
    except Denuncia.DoesNotExist:
        messages.error(request, "La denuncia no existe.")
        return redirect('/denuncias/')

# Procesar la edición
def procesarEdicionDenuncia(request, id):
    if request.method == 'POST':
        try:
            denuncia = Denuncia.objects.get(id=id)
            usuario_id = request.POST["usuario"]
            denuncia.usuario = Usuario.objects.get(id=usuario_id)
            denuncia.tipo_denuncia = request.POST["tipo_denuncia"]
            denuncia.descripcion = request.POST["descripcion"]
            denuncia.latitud = request.POST["latitud"]
            denuncia.longitud = request.POST["longitud"]
            denuncia.referencia = request.POST["referencia"]
            denuncia.estado = request.POST["estado"]

            # Si se subió un nuevo archivo, actualizar la evidencia
            if 'evidencia' in request.FILES:
                denuncia.evidencia = request.FILES['evidencia']

            denuncia.save()
            messages.success(request, "Denuncia actualizada exitosamente.")
            return redirect('/denuncias/')
        except Exception as e:
            messages.error(request, f"Error al actualizar la denuncia: {e}")
            return redirect(f'/denuncias/editarDenuncia/{id}/')
    else:
        messages.error(request, "Método no permitido.")
        return redirect('/denuncias/')
