from django.urls import path
from . import views

# my_tennis_club/members/urls.py
urlpatterns = [
    # Crie um arquivo chamado URLS.PY na mesma pasta 
    # do arquivo VIEWS.PY no aplicativo members 
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    # URLs Precisamos garantir que as URLs recebidas para 
    # /testing/ sejam redirecionadas para A visualização 
    # de teste.
    path('testing/', views.testing, name='testing.html'),
]