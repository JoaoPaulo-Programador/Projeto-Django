from django.urls import path
from . import views

urlpatterns = [
    path('cartoes/adicionar/', views.adicionar_cartao_view, name='adicionar_cartao'),
    path('cartoes/excluir/', views.excluir_cartao_view, name='excluir_cartao'),
]