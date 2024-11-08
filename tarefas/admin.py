from django.contrib import admin

from tarefas.models import Tarefa

# admin.site.register(Tarefa)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'data_inicio',
        'data_termino',
    )
