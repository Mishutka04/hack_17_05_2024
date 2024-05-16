from rest_framework import generics
from .models import Line, Negotiation, ReferenceDialog
from .serializers import LineSerializer, NegotiationSerializer, ReferenceDialogSerializer


class LineListAPIView(generics.ListAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class ReferenceDialogListAPIView(generics.ListAPIView):
    queryset = ReferenceDialog.objects.all()
    serializer_class = ReferenceDialogSerializer


class NegotiationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Negotiation.objects.all()
    serializer_class = NegotiationSerializer
