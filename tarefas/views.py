from rest_framework import generics

from tarefas.models import Tarefa
from tarefas.serializers import TarefaSerializer


class ListarCriarTarefaView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class EditarBuscarDeletarTarefaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

