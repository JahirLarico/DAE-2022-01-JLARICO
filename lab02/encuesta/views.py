from multiprocessing import context
from urllib import response
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo' : 'Formulario',
        'nombre' : 'Jahir Larico'
    }
    return render(request,'encuesta/formulario.html',context)
def enviar(request):
    context={
        'titulo':'Respuesta',
        'nombre':request.POST['nombre'],
        'clave':request.POST['password'],
        'educacion':request.POST['educacion'],
        'nacionalidad':request.POST['nacionalidad'],
        'idiomas':request.POST.getlist('idiomas'),
        'email':request.POST['email'],
        'website':request.POST['siitioweb']
    }
    return render(request,'encuesta/respuesta.html',context)
def operaciones(request):
    return render(request,'operaciones/formulario.html',context)
def resolver(request):
    context={
        'primer_numero':request.POST['primer_numero'],
        'segundo_numero':request.POST['segundo_numero'],
        'operacion':request.POST['operacion'],
    }
    return render(request,'operaciones/resolver.html',context)