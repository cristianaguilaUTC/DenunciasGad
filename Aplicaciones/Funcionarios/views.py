from django.shortcuts import render, redirect
from .models import Funcionario
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Mostrar listado de funcionarios
def inicioF(request):
    listadoFuncionarios = Funcionario.objects.all()
    return render(request, "inicioF.html", {'funcionarios': listadoFuncionarios})

# Mostrar formulario nuevo funcionario
def nuevoFuncionario(request):
    return render(request, "nuevoFuncionario.html")

# Guardar nuevo funcionario
def guardarFuncionario(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        correo = request.POST["correo"]
        contrasena_plana = request.POST["contrasena"]

        # Hasheando la contraseña antes de guardar
        contrasena_hasheada = make_password(contrasena_plana)

        try:
            Funcionario.objects.create(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                contrasena=contrasena_hasheada
            )
            messages.success(request, "Funcionario guardado exitosamente.")
            return redirect('inicio_funcionarios')
        except Exception as e:
            messages.error(request, f"Error al guardar el funcionario: {e}")
            return redirect('nuevo_funcionario')
    else:
        messages.error(request, "Método no permitido.")
        return redirect('inicio_funcionarios')

# Eliminar funcionario
def eliminarFuncionario(request, id):
    try:
        funcionarioEliminar = Funcionario.objects.get(id=id)
        funcionarioEliminar.delete()
        messages.success(request, "Funcionario eliminado exitosamente.")
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionario no encontrado.")
    return redirect('inicio_funcionarios')

# Mostrar formulario de edición
def editarFuncionario(request, id):
    try:
        funcionarioEditar = Funcionario.objects.get(id=id)
        return render(request, "editarFuncionario.html", {'funcionarioEditar': funcionarioEditar})
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionario no encontrado.")
        return redirect('inicio_funcionarios')

# Procesar edición
def procesarEdicionFuncionario(request, id):
    if request.method == 'POST':
        try:
            funcionario = Funcionario.objects.get(id=id)
            funcionario.nombre = request.POST["nombre"]
            funcionario.apellido = request.POST["apellido"]
            funcionario.correo = request.POST["correo"]

            nueva_contrasena = request.POST.get("contrasena", "").strip()
            if nueva_contrasena:
                funcionario.contrasena = make_password(nueva_contrasena)

            funcionario.save()
            messages.success(request, "Funcionario actualizado exitosamente.")
            return redirect('inicio_funcionarios')
        except Funcionario.DoesNotExist:
            messages.error(request, "Funcionario no encontrado.")
            return redirect('inicio_funcionarios')
    else:
        messages.error(request, "Método no permitido.")
        return redirect('inicio_funcionarios')
