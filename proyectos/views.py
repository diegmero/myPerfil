from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Proyecto

class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'proyectos/lista_proyectos.html'
    context_object_name = 'proyectos'

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyectos/detalle_proyecto.html'
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tecnologias_list'] = self.object.get_tecnologias_list()
        return context