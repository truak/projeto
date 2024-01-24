from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    #Alunos
    path('listar_alunos', views.listarAlunos, name='listar_alunos'),



    #Cursos
    path('listar_cursos', views.listarCursos, name='listar_cursos')
]