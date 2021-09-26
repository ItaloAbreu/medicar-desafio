from rest_framework import routers
from consultas.views import ConsultaViewSet 
from consultas.views import AgendaViewSet 

router = routers.SimpleRouter()
router.register(r'consultas', ConsultaViewSet, basename='consultas')
router.register(r'agendas', AgendaViewSet, basename='agendas')
