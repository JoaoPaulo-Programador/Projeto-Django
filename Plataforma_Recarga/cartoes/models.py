from django.db import models
from usuarios.models import Usuario


class Cartao(models.Model):
    CIDADES = [
        ('Petrolina', 'Petrolina'),
        ('Juazeiro', 'Juazeiro'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero = models.CharField(max_length=30)
    cidade = models.CharField(max_length=20, choices=CIDADES)
    apelido = models.CharField(max_length=50, blank=True, null=True)
    saldo = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.apelido or "Cartão"} - {self.numero}'