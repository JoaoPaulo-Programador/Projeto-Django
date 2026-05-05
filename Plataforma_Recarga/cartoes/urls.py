from django.urls import path
from . import views

urlpatterns = [
    path('cartoes/adicionar/', views.adicionar_cartao_view, name='adicionar_cartao'),
]