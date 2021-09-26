from rest_framework import routers
from consultas.views import ConsultaViewSet

router = routers.SimpleRouter()
router.register(r'consultas', ConsultaViewSet, basename='consultas')
