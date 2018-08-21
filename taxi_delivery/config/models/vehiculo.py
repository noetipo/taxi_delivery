from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class TipoVehiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        """
        docs
        """
        verbose_name = "TipoVehiculo"
        verbose_name_plural = "TipoVehiculos"

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    """
    docs
    """

    TIPO_USUARIO = (
        (u'1', u'Gerente'),
        (u'2', u'Tesorero'),
        (u'3', u'Cliente'),
        (u'4', u'Conductor'),
         )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    documento_identidad=models.IntegerField()
    foto_vehiculo=models.ImageField(upload_to='photo')
    conductor =models.ForeignKey(User, on_delete=models.CASCADE,)
    marca=models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        docs
        """
        verbose_name = "DatosPersonal"
        verbose_name_plural = "DatosPersonales"

    def __str__(self):
        return self.documento_identidad
