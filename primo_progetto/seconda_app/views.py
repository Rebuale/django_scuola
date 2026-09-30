from django.shortcuts import render

# Create your views here.
def es_if(request):
    dic = { 'var1' : 200, 'var2' : 200, 'var3' : 300 }
    return render(request, "seconda_app/es_if.html", dic)
def if_else_elif(request):
    vars = {'var1' : 20, 'var2' : 200}
    return render(request, "seconda_app/if_else_elif.html", vars)