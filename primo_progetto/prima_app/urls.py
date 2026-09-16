from django.urls import path
from prima_app.views import homepage

app_name = "prima_app"
urlpatterns = [
    path('', homepage, name = 'homepage'),
]