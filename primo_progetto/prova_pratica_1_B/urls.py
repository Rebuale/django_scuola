from django.urls import path
from prova_pratica_1_B.views import index, massimo, pari, studenti

app_name = "prova_pratica_1_B"
urlpatterns = [
    path('', index, name = 'index'),
    path('massimo', massimo, name = 'massimo'),
    path('pari', pari, name = 'pari'),
    path('studenti', studenti, name = 'studenti'),
]