from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# inclui todos os aplicativos ao projeto
urlpatterns = [
    path('admin/', admin.site.urls),
    # inclui o arquivo urls do aplicativo pacientes ao projeto
    path('pacientes/', include('pacientes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
