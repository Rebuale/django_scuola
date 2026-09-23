from django.urls import path
from prima_app.views import homepage, welcome, lista, chi_siamo, variabili

app_name = "prima_app"
urlpatterns = [
    path('', homepage, name = 'homepage'), #Gli apici vuoti servono per visualizzare solo la pagina base
    path('welcome', welcome, name = 'welcome'),  
    path('lista', lista, name = 'lista'),
    path('chi_siamo', chi_siamo, name = 'chi_siamo'),
    path('variabili', variabili, name ='variabili'),
]