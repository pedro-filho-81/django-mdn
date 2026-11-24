from django.urls import path
from . import views

# cria alista de urls
urlpatterns = [
    # inclui o arquivo views.py do aplicativo pacientes
    path('', views.pacientes, name='pacientes'),
    path('<int:id>', views.paciente_view, name='paciente_view'),
    path('atualizar_paciente/<int:id>', views.atualizar_paciente, name='atualizar_paciente'),
] # end lista