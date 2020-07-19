from django import forms

from .models import Item,OlxItem, Perfil

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title', 'description')

class OlxItemForm(forms.ModelForm):

    class Meta:
        model = OlxItem
        fields = ('title', 'description')

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('nome',)