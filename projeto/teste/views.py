from django.shortcuts import redirect, render
from django.http import HttpResponse
#from teste.forms import AlunoForm

from teste.models import Aluno, Curso

# Create your views here.
def index(request):
    return HttpResponse("Olá, Mundo! Agora é na Web.")

def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})



def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos': cursos})
