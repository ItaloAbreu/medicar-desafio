from rest_framework import routers
from medicos.views import EspecialidadeViewSet
from medicos.views import MedicoViewSet

router = routers.SimpleRouter()
router.register(r'especialidades', EspecialidadeViewSet, basename='especialidades')
router.register(r'medicos', MedicoViewSet, basename='medicos')
