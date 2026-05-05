from django.shortcuts import render

def adicionar_cartao_view(request):
    return render(request, 'cartoes/adicionar_cartao.html')