from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Proyecto, ImagenProyecto

class ImagenProyectoInline(admin.TabularInline):
    model = ImagenProyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    inlines = [ImagenProyectoInline]