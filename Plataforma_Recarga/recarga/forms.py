from django import forms
from .models import Recarga


class RecargaForm(forms.ModelForm):
    class Meta:
        model = Recarga
        fields = ['cartao', 'valor', 'forma_pagamento']