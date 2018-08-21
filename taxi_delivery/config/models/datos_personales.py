from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class DatosPersonal(models.Model):
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
    foto=models.ImageField(upload_to='photo', null=True,blank=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE,)
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO, default=3)
    direccion = models.TextField(null=True, blank=True)
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
