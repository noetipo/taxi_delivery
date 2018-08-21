

from rest_framework import serializers, viewsets
from ..models.datos_personales import *
class DatosPersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatosPersonal
        fields = '__all__'

class DatosPersonalViewSet(viewsets.ModelViewSet):
    queryset = DatosPersonal.objects.all()
    serializer_class = DatosPersonalSerializer