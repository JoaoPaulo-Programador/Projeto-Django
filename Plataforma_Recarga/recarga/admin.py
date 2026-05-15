from django.contrib import admin
from .models import Recarga


@admin.register(Recarga)
class RecargaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'cartao', 'valor', 'forma_pagamento', 'status', 'data')
    search_fields = ('usuario__nome', 'cartao__numero')
    list_filter = ('forma_pagamento', 'status', 'data')

    def save_model(self, request, obj, form, change):
        if change:
            recarga_antiga = Recarga.objects.get(pk=obj.pk)

            if recarga_antiga.status == 'Aprovado':
                cartao_antigo = recarga_antiga.cartao
                cartao_antigo.saldo -= recarga_antiga.valor
                cartao_antigo.save()

        super().save_model(request, obj, form, change)

        if obj.status == 'Aprovado':
            cartao = obj.cartao
            cartao.saldo += obj.valor
            cartao.save()

    def delete_model(self, request, obj):
        if obj.status == 'Aprovado':
            cartao = obj.cartao
            cartao.saldo -= obj.valor
            cartao.save()

        super().delete_model(request, obj)