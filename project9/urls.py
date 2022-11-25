"""project9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
from app2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1_if/',a1_if,name='a1_if'),
    path('a1_ifelif/',a1_ifelif,name='a1_ifelif'),
    path('a2_nested/',a2_nested,name='a2_nested'),
    path('a2_forloop/',a2_forloop,name='a2_forloop'),
]
