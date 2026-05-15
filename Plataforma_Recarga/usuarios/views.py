from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email)

            if check_password(senha, usuario.senha):
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nome'] = usuario.nome

                return redirect('dashboard')
            else:
                erro = 'Senha incorreta.'

        except Usuario.DoesNotExist:
            erro = 'Usuário não encontrado.'

        return render(request, 'usuarios/login.html', {'erro': erro})

    return render(request, 'usuarios/login.html')


def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if nome and email and senha:
            if Usuario.objects.filter(email=email).exists():
                erro = 'Este email já está cadastrado.'
                return render(request, 'usuarios/cadastro.html', {'erro': erro})

            usuario = Usuario(
                nome=nome,
                email=email,
                senha=make_password(senha)
            )
            usuario.save()

            return redirect('login')

    return render(request, 'usuarios/cadastro.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')