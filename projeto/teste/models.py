from django.db import models


class Aluno(models.Model):
    nome = models.CharField(null = False, max_length = 200)
    cpf = models.CharField(null = False, max_length = 11)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome + " - " + self.email


class Curso(models.Model):
    nome = models.CharField(null = False, max_length = 30)
    carga_horaria = models.IntegerField(null = False)
    investimento = models.DecimalField(null = False, max_digits = 8, decimal_places = 2)
    
    def __str__(self):
        return self.nome
