from django.contrib import admin
from .models import Pacientes

# adiciona o aplicativo Pacientes na página de administração
admin.site.register(Pacientes)