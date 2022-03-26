from multiprocessing import context
from unittest import result
from urllib import response
from django.shortcuts import render
def index(request):
    return render(request,'volumen/index.html')
def volumen(request):
    radio=int(request.POST['radio'])
    altura=int(request.POST['altura'])
    area_base=3.1416*radio*radio
    volumen=area_base*altura
    context={
        'radio':radio,
        'altura':altura,
        'volumen':volumen
    }
    return render(request,'volumen/volumen.html',context)