from django.conf.urls import url, include
from rest_framework import routers
from .views.empresa import EmpresaViewSet
from .views.datos_personales import DatosPersonalViewSet
from .views.vehiculo import VehiculoViewSet
from .views.tipo_vehiculo import TipoVehiculoViewSet
router = routers.DefaultRouter()

router.register(r'empresa', EmpresaViewSet)
router.register(r'datos-personal', DatosPersonalViewSet)
router.register(r'tipo-vehiculo', DatosPersonalViewSet)
router.register(r'vehiculo', VehiculoViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
