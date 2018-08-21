from rest_framework import serializers, viewsets
from ..models.vehiculo import Vehiculo
class TVehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehiculo
        fields = '__all__'

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = Vehiculo