import requests
from django.shortcuts import render, redirect
from .forms import ItemForm, OlxItemForm, PerfilForm
from .models import Item, OlxItem, TwitterItem, Perfil
from bs4 import BeautifulSoup
from . import models
from requests.compat import quote_plus
from .TtScraper import TtScraper

# Create your views here.

BASE_OLX_URL = 'https://rj.olx.com.br/?q={}'

def home(request):
    return render(request, 'myapp/index.html')


def new_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save()
            return redirect('/new_item')

    else:
        form = ItemForm()
        items_select = Item.objects.all()
        stuff_from_frontend = {
            'form': form,
            'items': items_select,

        }
        return render(request, 'myapp/new_item.html', stuff_from_frontend)

def new_olx_item(request):
    #olx_item = request.POST.get('new_olx_item')
    olx_item = OlxItemForm(request.POST)

    if olx_item.is_valid():
        olx_item_add = olx_item.save()
        return redirect('/new_item')
    #models.OlxItem.objects.create(title=olx_item.item)
    final_url = BASE_OLX_URL.format(quote_plus(olx_item))
    print(final_url)

    response = requests.get('https://rj.olx.com.br/?q=aluguel')
    data = response.text
    print(data)

    olx_items_select = Item.objects.all()
    stuff_from_frontend = {
        'form': form,
        'olx_items': olx_items_select,
    }
    return render(request, 'myapp/new_item.html', stuff_from_frontend)

def listaOlx(request):
    olx_query ='https://rj.olx.com.br/?q=aluguel'

    olx_items_select = OlxItem.objects.all()


    stuff_from_frontend = {
        'olx_items': olx_items_select,
    }

    return render(request, 'myapp/listaOlx.html', stuff_from_frontend)

def listaTwitter(request):

    response = requests.get('https://twitter.com/search?q=brasil&src=typed_query')
    tt_data = response.text

    tt_data_soup = BeautifulSoup(tt_data, features='html.parser')

    tweet_titles = tt_data_soup.find_all('a', {'class': 'css-4rbku5'})

    print(tweet_titles)
    ttscp = TtScraper('Mario', 'MauroWebeer')

    # teste comeca aqui

    print("user: " + ttscp.user + "  nomeDoObjeto:  " + ttscp.title)
    print(ttscp.df)
    for cols in ttscp.df.columns:
        print(cols)

    itter = ttscp.df.itertuples

    print("aqui esta o itttteer:  " + str(itter) + " e aqui finalizaaaa")

    print(ttscp.df.loc[0,'text'])

    for dftest in ttscp.df.head().itertuples():
        print(dftest.text)

    #e termina aqui!!!
    tt_items_select = TwitterItem.objects.all()

    stuff_from_frontend = {
        'tt_items': tt_items_select,
        'tweet_obj': ttscp.df.head().itertuples(),
        'tt_user': ttscp.user,
    }

    return render(request, 'myapp/listaTwitter.html', stuff_from_frontend)


def cadastrarPerfil(request):

    if request.method == 'POST':
        formPerfil = PerfilForm(request.POST)

        if formPerfil.is_valid():
            itemPerfil = formPerfil.save()
            return redirect('/')

    else:
        formPerfil = PerfilForm()
        perfil_select = Perfil.objects.all()
        stuff_from_frontend = {
            'form' : formPerfil,
            'perfis' : perfil_select,
        }

    return render(request, 'myapp/cadastrarPerfil.html', stuff_from_frontend)


