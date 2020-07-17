import requests
from django.shortcuts import render, redirect
from .forms import ItemForm, OlxItemForm
from .models import Item, OlxItem, TwitterItem
from bs4 import BeautifulSoup
from . import models
from requests.compat import quote_plus

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
    #search = request.POST.get('search')
    #tt_search = request.POST.get('')
    tt_query = 'https://twitter.com/search?q=brasil&src=typed_query'

    #response = requests.get('https://rio.craigslist.org/search/hhh?query=copacabana&sort=rel')
    response = requests.get('https://twitter.com/search?q=brasil&src=typed_query')
    tt_data = response.text

    tt_data_soup = BeautifulSoup(tt_data, features='html.parser')

    tweet_titles = tt_data_soup.find_all('a', {'class': 'css-4rbku5'})
    #tweet_titles = tt_data_soup.find_all('a', {'class': 'result-title'})

    print(tweet_titles)

    #response = requests.get('https://rio.craigslist.org/search/hhh?query=copacabana&sort=rel')
    #data = response.text
    #soup = BeautifulSoup(data, features='html.parser')
    #post_titles = soup.find_all('a', {'class': 'result-title'})
    #print(post_titles[0].get('href'))


    tt_items_select = TwitterItem.objects.all()

    stuff_from_frontend = {
        'tt_items': tt_items_select,
    }

    return render(request, 'myapp/listaTwitter.html', stuff_from_frontend)