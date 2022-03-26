from multiprocessing import context
from unittest import result
from urllib import response
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'operaciones/formulario.html')
def resolver(request):
    opera=request.POST['operacion']
    num_1=int(request.POST['primer_numero'])
    num_2=int(request.POST['segundo_numero'])
    resultado=0
    if opera=="Suma":
        resultado=num_1+num_2
        simbolo="+"
    elif opera=="Resta":
        resultado=num_1-num_2
        simbolo="-"
    elif opera=="Multiplicacion":
        resultado=num_1*num_2
        simbolo="*"
    elif opera=="Division":
        resultado=num_1/num_2
        simbolo="/"
    context={
        'primer_numero':request.POST['primer_numero'],
        'segundo_numero':request.POST['segundo_numero'],
        'operacion':request.POST['operacion'],
        'resultado':resultado,
        'simbolo':simbolo
    }
    return render(request,'operaciones/resolver.html',context)