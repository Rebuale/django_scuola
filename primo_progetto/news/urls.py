from django.urls import path
from .views import home, articoloDetailsView
app_name="news"
urlpatterns = [
    path("",home,name="homepage"),
    path("articolo/<int:pk>", articoloDetailsView, name="articolo_details")
]