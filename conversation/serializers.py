from rest_framework import serializers
from .models import Line, Negotiation, ReferenceDialog


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = '__all__'


class ReferenceDialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceDialog
        fields = '__all__'


class NegotiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negotiation
        fields = '__all__'
