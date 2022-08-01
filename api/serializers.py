from rest_framework import serializers
from prijemka.models import Artikul

class ArtikulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikul
        fields = "__all__"

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artikul
        fields = ["code", "in_field"]

