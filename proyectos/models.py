from django.db import models

# Create your models here.
from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=200)
    imagen_principal = models.ImageField(upload_to='proyectos/')
    url = models.URLField(blank=True)
    github = models.URLField(blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_tecnologias_list(self):
        return [tech.strip() for tech in self.tecnologias.split(',')]

class ImagenProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='proyectos/')