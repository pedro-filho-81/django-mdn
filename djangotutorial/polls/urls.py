from django.urls import path

from . import views
'''
# o valor 'name' conforme chamado pela tag de modelo {% url %}
path("<int:question_id>/", views.detail, name="detail"),

# adicionou a palavra 'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
'''
app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]