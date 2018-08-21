import logging

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from ..models.empresa import *


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = '__all__'

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer