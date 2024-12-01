from rest_framework import viewsets
from .models import NotaFiscal
from .serializers import NotaFiscalSerializer

class NotaFiscalViewSet(viewsets.ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer