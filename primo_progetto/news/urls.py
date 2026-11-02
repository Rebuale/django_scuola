from django.urls import path
from .views import home, articoloDetailsView, listaArticoli
app_name="news"
urlpatterns = [
    path("",home,name="homepage"),
    path("articolo/<int:pk>", articoloDetailsView, name="articolo_details"),
    path("lista_articoli/", listaArticoli, name="lista_articoli"),
    path("lista_articoli/<int:pk>", articoloDetailsView, name="lista_articoli_dettaglio"),
    path("giornalista/<int:pk>/articoli/", listaArticoli, name="lista_articoli_giornalista"),
]