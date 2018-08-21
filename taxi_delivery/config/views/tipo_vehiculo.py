
from rest_framework import serializers, viewsets
from ..models.vehiculo import TipoVehiculo
class TipoVehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoVehiculo
        fields = '__all__'

class TipoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = TipoVehiculo.objects.all()
    serializer_class = TipoVehiculoSerializer