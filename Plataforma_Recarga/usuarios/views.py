from django.shortcuts import render
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # aqui ainda é simulação
        # depois você conecta com banco

        if email and senha:
            return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if nome and email and senha:
            return redirect('login')

    return render(request, 'usuarios/cadastro.html')