from django.shortcuts import render, redirect
from calculator import calculator
from .serializers import CalculatorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Consumer
from .serializers import ConsumerSerializer
from rest_framework import viewsets



def calcularConsumo(request):
    if request.method == 'POST':
        consumo1 = float(request.POST.get('consumo1', 0))
        consumo2 = float(request.POST.get('consumo2', 0))
        consumo3 = float(request.POST.get('consumo3', 0))
        tarifa = float(request.POST.get('tarifa', 0))
        tipoTarifa = request.POST.get('tipo', '')  

        result = calculator([consumo1, consumo2, consumo3], tarifa, tipoTarifa)

        return render(request, 'index.html', {
            'result': result,
            'economia_anual': result[0],  
            'economia_mensal': result[1], 
            'desconto_aplicado': result[2], 
            'cobertura': result[3], 
        })

    return render(request, 'index.html')


class CalculatorAPIView(APIView):
    def post(self, request, format=None):
        serializer = CalculatorSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            consumo = [data['consumo1'], data['consumo2'], data['consumo3']]
            tarifa = data['tarifa']
            tipo_tarifa = data['tipo_tarifa']
            result = calculator(consumo, tarifa, tipo_tarifa)
            return Response({
                'economia_anual': result[0],
                'economia_mensal': result[1],
                'desconto_aplicado': result[2],
                'cobertura': result[3],
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer    


def cadastrar_consumidor(request):
    if request.method == 'POST':
        # Receber os dados do formulário
        name = request.POST.get('name')
        document = request.POST.get('document')
        zip_code = request.POST.get('zip_code')
        city = request.POST.get('city')
        state = request.POST.get('state')
        consumption = request.POST.get('consumption')
        distributor_tax = request.POST.get('distributor_tax')

        consumer = Consumer.objects.create(
            name=name,
            document=document,
            zip_code=zip_code,
            city=city,
            state=state,
            consumption=consumption,
            distributor_tax=distributor_tax
        )
        return redirect('sucesso')
    else:
        return render(request, 'consumer.html')
    
def sucesso(request):
    return render(request, 'sucesso.html')