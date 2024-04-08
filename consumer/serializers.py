from rest_framework import serializers
from .models import Consumer



class CalculatorSerializer(serializers.Serializer):
    consumo1 = serializers.FloatField()
    consumo2 = serializers.FloatField()
    consumo3 = serializers.FloatField()
    tarifa = serializers.FloatField()
    tipo_tarifa = serializers.CharField()

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['name', 'document', 'zip_code', 'city', 'state', 'consumption', 'distributor_tax']    


