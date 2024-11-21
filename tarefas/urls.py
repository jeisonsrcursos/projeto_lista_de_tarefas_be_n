from django.urls import path
from rest_framework import routers

from tarefas.views import ListarCriarTarefaView, EditarBuscarDeletarTarefaView, TarefaView


# API V1
urlpatterns = [
    path(
        'tarefa/',
        ListarCriarTarefaView.as_view(),
        name='listar-criar-tarefa-view'
    ),
    path(
        'tarefa/<int:pk>',
        EditarBuscarDeletarTarefaView.as_view(),
        name='editar-buscar-deletar-tarefa-view'
    )
]

# API V2
router = routers.DefaultRouter();
router.register(r'tarefa', TarefaView, basename='crud-tarefas')
