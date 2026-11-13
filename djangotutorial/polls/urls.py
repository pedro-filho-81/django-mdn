from django.urls import path
# do aplicativo atual(polls) importe o arquivo views
from . import views

urlpatterns = [
    # do arquivo views chama a função index
    path('', views.index, name='index')
]