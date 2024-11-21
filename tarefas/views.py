from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from tarefas.models import Tarefa
from tarefas.serializers import TarefaSerializer

# API V1
class ListarCriarTarefaView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


class EditarBuscarDeletarTarefaView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


# API V2
class TarefaView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer


