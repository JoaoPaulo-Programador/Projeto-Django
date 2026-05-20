from django import forms
from .models import Cartao


class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ['numero', 'cidade', 'apelido']