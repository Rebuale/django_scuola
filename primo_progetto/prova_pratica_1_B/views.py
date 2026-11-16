from django.shortcuts import render
import random

# Create your views here.
def massimo(request):
    vars = {'var1' : random.randint(1,20), 'var2' : random.randint(1,20), 'var3' : random.randint(1,20) }
    return render(request, "prova_pratica_1_B/massimo.html", vars)

def pari(request):
    lista = []
    for _ in range(30):
        lista.append(random.randint(1,20))
    i = 0
    for x in lista:
        if x%2 == 0:
            i+=1
    dic = {"lista" : lista, "i" : i}
    return render(request, "prova_pratica_1_B/pari.html", dic)

def studenti(request):
    dic = {"studenti" : {"Paolo Balzarotti": True, "Morgan Gerevini": False, "Alessandro Rebuscini": True}}
    return render(request, "prova_pratica_1_B/studenti.html", dic)

def index(request):
    return render(request, "prova_pratica_1_B/index.html")

