from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "prima_app/homepage.html")
def welcome(request):
    return render(request, "prima_app/welcome.html")
def lista(request):
    return render(request, "prima_app/lista.html")
def chi_siamo(request):
    return render(request, "prima_app/chi_siamo.html")
def variabili(request):
    context = {"var1" : "10", "var2" : "ciao", "var3" : "123 hello world"}
    return render (request, "prima_app/variabili.html", context)