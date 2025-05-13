from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CadastroUsuarioForm

def index(request):
    return render(request, 'index/index.html')




# Create your views here.
