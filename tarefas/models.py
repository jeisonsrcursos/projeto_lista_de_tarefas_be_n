from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=160)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    concluido = models.BooleanField()

    def __str__(self):
        return self.titulo
