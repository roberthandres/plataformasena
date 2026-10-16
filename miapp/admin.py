from django.contrib import admin
from .models import Programa, Instructor, Aprendiz, Competencia

admin.site.register(Programa)
admin.site.register(Instructor)
admin.site.register(Aprendiz)
admin.site.register(Competencia)
