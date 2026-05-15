from decimal import Decimal, InvalidOperation

from django.shortcuts import render, redirect
from usuarios.models import Usuario
from cartoes.models import Cartao
from .models import Recarga


def dashboard_view(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    cartoes = Cartao.objects.filter(usuario=usuario)

    recargas = Recarga.objects.filter(
        usuario=usuario,
        status='Aprovado'
    ).order_by('-data')

    return render(request, 'recarga/dashboard.html', {
        'usuario_nome': usuario.nome,
        'cartoes': cartoes,
        'recargas': recargas
    })


def recarga_view(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    usuario = Usuario.objects.get(id=request.session['usuario_id'])
    cartoes = Cartao.objects.filter(usuario=usuario)

    if request.method == 'POST':
        cartao_id = request.POST.get('cartao_id')
        valor = request.POST.get('valor')
        forma_pagamento = request.POST.get('forma_pagamento')

        if not cartao_id or not valor or not forma_pagamento:
            return render(request, 'recarga/recarga.html', {
                'cartoes': cartoes,
                'erro': 'Preencha todos os campos.'
            })

        try:
            cartao = Cartao.objects.get(id=cartao_id, usuario=usuario)
            valor_decimal = Decimal(valor)

        except Cartao.DoesNotExist:
            return render(request, 'recarga/recarga.html', {
                'cartoes': cartoes,
                'erro': 'Cartão não encontrado.'
            })

        except InvalidOperation:
            return render(request, 'recarga/recarga.html', {
                'cartoes': cartoes,
                'erro': 'Valor inválido.'
            })

        Recarga.objects.create(
            usuario=usuario,
            cartao=cartao,
            valor=valor_decimal,
            forma_pagamento=forma_pagamento,
            status='Aprovado'
        )

        cartao.saldo += valor_decimal
        cartao.save()

        return redirect('dashboard')

    return render(request, 'recarga/recarga.html', {
        'cartoes': cartoes
    })