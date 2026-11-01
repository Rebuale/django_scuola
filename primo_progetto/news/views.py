from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse
from .models import Articolo, Giornalista

# Create your views here.
"""
def home(request):
    a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")
    for gio in Giornalista.objects.all():
        g += (gio.nome + "<br>")
    response = "Articoli:<br>" + a + "<br>Gioranlisti:<br>" +g
    return HttepResponse("<h1>" + response + "</h1>")
"""
"""
def home(request):
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo + "<br>")
    for gio in Giornalista.objects.all():
        g.append(gio.nome + "<br>")
    response = str(a) + "<br>" + str(g)
    return HttepResponse("<h1>" + response + "</h1>")

"""
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "news/homepage.html", context)

def articoloDetailsView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo" : articolo}
    return render(request, "news/articolo_details.html", context)
