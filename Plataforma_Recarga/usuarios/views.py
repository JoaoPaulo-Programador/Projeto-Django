from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from .models import Usuario
from .forms import UsuarioForm


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

        return render(request, 'usuarios/login.html', {
            'erro': erro
        })

    return render(request, 'usuarios/login.html')


def cadastro_view(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():

            usuario = form.save(commit=False)

            usuario.senha = make_password(
                form.cleaned_data['senha']
            )

            usuario.save()

            return redirect('login')

    else:
        form = UsuarioForm()

    return render(request, 'usuarios/cadastro.html', {
        'form': form
    })


def logout_view(request):
    request.session.flush()
    return redirect('login')