from django.contrib import admin
from .models import Aluno
from .models import Curso

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Curso)
