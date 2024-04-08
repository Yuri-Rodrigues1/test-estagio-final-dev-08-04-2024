from django.contrib import admin
from django.urls import path, include
from consumer.views import calcularConsumo, CalculatorAPIView, ConsumerViewSet, sucesso,cadastrar_consumidor
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'consumers', ConsumerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calcularConsumo, name='index'),  
    path('api/calculadora/', CalculatorAPIView.as_view(), name='calculadora_api'),  
    path('api/', include(router.urls)),  
    path('cadastrar_consumidor/', cadastrar_consumidor, name='cadastrar_consumidor'),
    path('sucesso/', sucesso, name='sucesso')
]