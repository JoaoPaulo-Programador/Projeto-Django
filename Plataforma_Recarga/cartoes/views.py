from django.shortcuts import render, redirect
from usuarios.models import Usuario
from .models import Cartao


def adicionar_cartao_view(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    if request.method == 'POST':
        numero_cartao = request.POST.get('numero_cartao')
        cidade = request.POST.get('cidade')
        apelido = request.POST.get('apelido')

        usuario = Usuario.objects.get(id=request.session['usuario_id'])

        Cartao.objects.create(
            usuario=usuario,
            numero=numero_cartao,
            cidade=cidade,
            apelido=apelido,
            saldo=0.00
        )

        return redirect('dashboard')

    return render(request, 'cartoes/adicionar_cartao.html')


def excluir_cartao_view(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    usuario = Usuario.objects.get(id=request.session['usuario_id'])

    Cartao.objects.filter(usuario=usuario).delete()

    return redirect('dashboard')