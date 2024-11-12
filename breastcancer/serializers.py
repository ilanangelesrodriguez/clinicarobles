from rest_framework import serializers
from .models import Examen, Prediccion

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'

class PrediccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediccion
        fields = '__all__'
        