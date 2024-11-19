from rest_framework import generics, viewsets

from tarefas.models import Tarefa
from tarefas.serializers import TarefaSerializer

# API V1
class ListarCriarTarefaView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class EditarBuscarDeletarTarefaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


# API V2
class TarefaView(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


