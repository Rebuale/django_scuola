from django.urls import path
from seconda_app.views import es_if

app_name = "seconda_app"
urlpatterns = [
    path('es_if', es_if, name = 'es_if'), #Gli apici vuoti servono per visualizzare solo la pagina base
]