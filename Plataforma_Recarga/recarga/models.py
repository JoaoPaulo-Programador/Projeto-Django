from django.db import models
from usuarios.models import Usuario
from cartoes.models import Cartao


class Recarga(models.Model):
    FORMAS_PAGAMENTO = [
        ('Pix', 'Pix'),
        ('Cartão', 'Cartão'),
        ('Boleto', 'Boleto'),
    ]

    STATUS = [
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Cancelado', 'Cancelado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20, choices=FORMAS_PAGAMENTO)
    status = models.CharField(max_length=20, choices=STATUS, default='Aprovado')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Recarga de R$ {self.valor} - {self.status}'