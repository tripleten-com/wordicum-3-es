"""Configuración de la URL de wordicum

La lista `urlpatterns` enruta URLs a vistas. Para más información, consulta:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Ejemplos:
Vistas de función
    1. Añade una importación: from my_app import views
    2. Añade una URL a urlpatterns: path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega una importación: from other_app.views import Home
    2. Agrega una URL a urlpatterns: path('', Home.as_view(), name='home')
Incluir otra URLconf
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
