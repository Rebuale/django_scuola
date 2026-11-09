import datetime

from django.shortcuts import render, get_object_or_404
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

def index(request):
    context = {"articoli": Articolo.objects.all()}
    return render(request, "news/index.html", context)

def articoloDetailsView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo" : articolo}
    return render(request, "news/articolo_details.html", context)

def listaArticoli(request, pk=None):
    giornalista = None
    if pk is None:
        articoli = Articolo.objects.all()
    else:
        giornalista = get_object_or_404(Giornalista, pk=pk)
        articoli = Articolo.objects.filter(giornalista__pk=pk)

    context = {"articoli": articoli, "giornalista": giornalista}
    return render(request, "news/lista_articoli.html", context)

def queryBase(request):
    # Tutti gli articoli scritti da giornalisti di un certo cognome.
    articoli_cognome = Articolo.objects.filter(giornalista__cognome="Rossi")
    numero_totale = Articolo.objects.count()

    # Numero di articoli scritti dal giornalista con ID 1.
    numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista_id=1).count()

    # Articoli ordinati per visualizzazioni decrescenti.
    articoli_ordinati = Articolo.objects.order_by("-visualizzazioni")

    # Articoli senza visualizzazioni.
    articoli_senza_visual = Articolo.objects.filter(visualizzazioni=0)

    # Articolo più visualizzato.
    articolo_piu_visualizzato = Articolo.objects.order_by("-visualizzazioni").first()

    # Giornalisti nati dopo una certa data.
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1))

    # Articoli pubblicati in una data specifica.
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023, 1, 1))

    # Articoli pubblicati in un intervallo di date.
    articoli_periodo = Articolo.objects.filter(data__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))

    # Articoli scritti da giornalisti nati prima del 1980.
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)

    # Giornalista più giovane.
    giornalista_giovane = Giornalista.objects.order_by('anno_di_nascita').first()

    # Giornalista più anziano.
    giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()

    # Ultimi 5 articoli pubblicati.
    ultimi = Articolo.objects.order_by('-data')[:5]

    # Articoli con almeno 100 visualizzazioni.
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    # Articoli che contengono una certa parola nel titolo.
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')

    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale': numero_totale,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visual': articoli_senza_visual,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
    }

    context['query_results'] = [
        {'label': 'Articoli di giornalisti con cognome Rossi', 'type': 'articles', 'value': articoli_cognome},
        {'label': 'Numero totale di articoli', 'type': 'count', 'value': numero_totale},
        {'label': 'Articoli del giornalista con ID 1', 'type': 'count', 'value': numero_articoli_giornalista_1},
        {'label': 'Articoli ordinati per visualizzazioni', 'type': 'articles', 'value': articoli_ordinati},
        {'label': 'Articoli senza visualizzazioni', 'type': 'articles', 'value': articoli_senza_visual},
        {'label': 'Articolo più visualizzato', 'type': 'article', 'value': articolo_piu_visualizzato},
        {'label': 'Giornalisti nati dopo il 1 gennaio 1990', 'type': 'journalists', 'value': giornalisti_data},
        {'label': 'Articoli pubblicati il 1 gennaio 2023', 'type': 'articles', 'value': articoli_del_giorno},
        {'label': 'Articoli pubblicati nel 2023', 'type': 'articles', 'value': articoli_periodo},
        {'label': 'Articoli di giornalisti nati prima del 1980', 'type': 'articles', 'value': articoli_giornalisti},
        {'label': 'Giornalista più giovane', 'type': 'journalist', 'value': giornalista_giovane},
        {'label': 'Giornalista più anziano', 'type': 'journalist', 'value': giornalista_anziano},
        {'label': 'Ultimi 5 articoli pubblicati', 'type': 'articles', 'value': ultimi},
        {'label': 'Articoli con almeno 100 visualizzazioni', 'type': 'articles', 'value': articoli_minime_visualizzazioni},
        {'label': 'Articoli con “importante” nel titolo', 'type': 'articles', 'value': articoli_parola},
    ]
    return render(request, "news/query.html", context)