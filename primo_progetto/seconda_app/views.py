from django.shortcuts import render
import datetime

# Create your views here.
def es_if(request):
    dic = { 'var1' : 200, 'var2' : 200, 'var3' : 300 }
    return render(request, "seconda_app/es_if.html", dic)
def if_else_elif(request):
    vars = {'var1' : 20, 'var2' : 200}
    return render(request, "seconda_app/if_else_elif.html", vars)
def es_for(request):
    dic ={"list1" : [1, datetime.date(2026,10,5), "Non mollare!"], "list2" : [2, datetime.date(2026,10,6), "Non mollare!"], 'my_dict' : {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'}}
    return render (request, "seconda_app/es_ciclo_for.html", dic)