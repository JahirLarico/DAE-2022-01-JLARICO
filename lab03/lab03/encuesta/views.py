from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pregunta, Opcion
# Create your views here.
def index(request):
    latest_question_list = Pregunta.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'encuesta/index.html', context)

def detalle(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, 'encuesta/detalle.html', {'pregunta': pregunta})

def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        opcion_id = request.POST['opcion']
        opcion = Opcion.objects.get(pk=opcion_id)
        opcion.votos += 1
        opcion.save()
        ##redirect to url
        url='/encuesta/'+str(pregunta_id)+'/'
        return HttpResponseRedirect(url)
    except (KeyError, Opcion.DoesNotExist):
        return render(request, 'encuesta/detalle.html', {
            'pregunta': pregunta,
            'error_message': "No se seleccionó ninguna opción",
        })   
def resultados(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, 'encuesta/resultados.html', {'pregunta': pregunta})
