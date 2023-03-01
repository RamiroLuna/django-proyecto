from django.shortcuts import render, redirect
from .models import informacionPersonal
from django.contrib import messages

# Create your views here.

def home(request):
    informacion = informacionPersonal.objects.all()
    return render(request, "alta_agenda.html", {"informacion": informacion})

def registrarDatos(request):
    nombre=request.POST['txtNombre']
    apellidoPaterno = request.POST['txtApePaterno']
    apellidoMaterno = request.POST['txtApeMaterno']
    fechaNacimiento = request.POST['txtFechaNacimiento']
    edad = request.POST['txtEdad']
    correoElectronico = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']

    informacion = informacionPersonal.objects.create(
        nombre=nombre, apellidoPaterno=apellidoPaterno,apellidoMaterno=apellidoMaterno, fechaNacimiento=fechaNacimiento,
        edad=edad, correoElectronico=correoElectronico, telefono=telefono)
    messages.success(request, '¡Datos registrados correctamente!')
    return redirect('/')

def edicionDatos(request, id):
    informacion = informacionPersonal.objects.get(id=id)
    return render(request, "editarDatos.html", {"informacion": informacion})

def editarDatos(request):
    id =request.POST['txtId']
    nombre = request.POST['txtNombre']
    apellidoPaterno = request.POST['txtApePaterno']
    apellidoMaterno = request.POST['txtApeMaterno']
    fechaNacimiento = request.POST['txtFechaNacimiento']
    edad = request.POST['txtEdad']
    correoElectronico = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']

    informacion = informacionPersonal.objects.get(id=id)
    informacion.nombre = nombre
    informacion.apellidoPaterno = apellidoPaterno
    informacion.apellidoMaterno = apellidoMaterno
    informacion.fechaNacimiento = fechaNacimiento
    informacion.edad = edad
    informacion.correoElectronico = correoElectronico
    informacion.telefono = telefono
    informacion.save()

    messages.success(request, '¡Datos actualizados correctamente!')
    return redirect('/')

def eliminarDatos(request, id):
    informacion = informacionPersonal.objects.get(id=id)
    informacion.delete()
    messages.success(request, '¡Datos eliminados correctamente!')
    return redirect('/')
