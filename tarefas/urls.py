from django.urls import path

from tarefas.views import ListarCriarTarefaView, EditarBuscarDeletarTarefaView

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
