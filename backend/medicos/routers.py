from rest_framework import routers
from medicos.views import EspecialidadeViewSet

router = routers.SimpleRouter()
router.register(r'especialidades', EspecialidadeViewSet, basename='especialidades')
