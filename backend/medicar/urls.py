"""medicar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy
from allauth.account.models import EmailAddress
from medicos.routers import router as router_medicos
from consultas.routers import router as router_consultas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest_auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += router_medicos.urls
urlpatterns += router_consultas.urls


admin.site.index_title = 'Medicar'
admin.site.site_header = 'Administração Medicar'
admin.site.site_title = 'Administração Medicar'
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(TokenProxy)
admin.site.unregister(EmailAddress)
