from django.contrib import admin
from .models import Item, OlxItem, TwitterItem, Perfil

# Register your models here.

admin.site.register(Item)
admin.site.register(OlxItem)
admin.site.register(TwitterItem)
admin.site.register(Perfil)