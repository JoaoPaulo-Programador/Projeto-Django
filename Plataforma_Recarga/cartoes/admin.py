from django.contrib import admin
from .models import Cartao


@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'numero', 'cidade', 'apelido', 'saldo')
    search_fields = ('numero', 'apelido', 'usuario__nome')
    list_filter = ('cidade',)