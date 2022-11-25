from django.shortcuts import render

# Create your views here.


def a2_nested(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'a2_nested.html',d)


def a2_forloop(request):
    d={'name':'Loki'}
    return render(request,'a2_forloop.html',d)