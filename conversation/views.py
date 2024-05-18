from rest_framework import generics
from .models import Line, Negotiation, ReferenceDialog
from .serializers import LineSerializer, NegotiationSerializer, ReferenceDialogSerializer


class LineListAPIView(generics.ListAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class ReferenceDialogListAPIView(generics.ListAPIView):
    serializer_class = ReferenceDialogSerializer

    def get_queryset(self, *args, **kwargs):
        if 'pk' in self.kwargs:
            return ReferenceDialog.objects.filter(pk=self.kwargs['pk'])
        return ReferenceDialog.objects.all()


class NegotiationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NegotiationSerializer

    def get_queryset(self, *args, **kwargs):
        if 'pk' in self.kwargs:
            return Negotiation.objects.filter(line=self.kwargs['pk'])
        return Negotiation.objects.all()


class NegotiationInfoList(generics.ListCreateAPIView):
    serializer_class = NegotiationSerializer

    def get_queryset(self, *args, **kwargs):
        if 'pk' in self.kwargs:
            return Negotiation.objects.filter(pk=self.kwargs['pk'])
        return Negotiation.objects.all()
