from django.urls import path
from .views import ProyectoListView, ProyectoDetailView

urlpatterns = [
    path('', ProyectoListView.as_view(), name='lista_proyectos'),
    path('<int:pk>/', ProyectoDetailView.as_view(), name='detalle_proyecto'),
]