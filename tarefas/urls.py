from django.urls import path
from rest_framework import routers

from tarefas.views import ListarCriarTarefaView, EditarBuscarDeletarTarefaView, TarefaView

router = routers.DefaultRouter();
router.register(r'tarefas', TarefaView, basename='crud-tarefas')

urlpatterns = [
    # API V1
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
