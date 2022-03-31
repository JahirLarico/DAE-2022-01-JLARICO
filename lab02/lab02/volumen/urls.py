from pydoc import resolve
from django.urls import path
from . import views
app_name='volumen'

urlpatterns=[
    path('',views.index,name='index'),
    path('volumen',views.volumen,name='volumen'),
]