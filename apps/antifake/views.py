from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroUsuarioForm
from django.contrib.auth import authenticate,login as auth_login, logout


def home(request):
    return render(request, 'home/home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login/login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'login/login.html')


def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'login/cadastro.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')
