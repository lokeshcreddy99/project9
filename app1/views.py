from django.shortcuts import render

# Create your views here.

def a1_if(request):
    d={'a':100,'b':200}
    return render(request,'a1_if.html',d)

def a1_ifelif(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'a1_ifelif.html',d)