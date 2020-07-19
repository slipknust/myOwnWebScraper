"""myOwnWebScraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_item', views.new_item, name="new_item"),
    path('new_olx_item', views.new_olx_item, name="new_olx_item"),
    path('listaOlx', views.listaOlx, name="listaOlx"),
    path('listaTwitter', views.listaTwitter, name="listaTwitter"),
    path('cadastrarPerfil', views.cadastrarPerfil, name="cadastrarPerfil"),
]
