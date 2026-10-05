from django.urls import path
from seconda_app.views import es_if, if_else_elif, es_for, index
app_name = "seconda_app"
urlpatterns = [
    path('', index, name = 'index'),
    path('es_if', es_if, name = 'es_if'), #Gli apici vuoti servono per visualizzare solo la pagina base
    path('if_else_elif', if_else_elif, name = 'if_else_elif'),
    path('es_ciclo_for', es_for, name = 'es_ciclo_for')
]