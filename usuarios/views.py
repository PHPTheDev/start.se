from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
# Create your views here.

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        conSenha = request.POST.get('confirmar_senha')

        if not senha == conSenha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
            return redirect('/usuarios/cadastro')
        
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                password=senha
            )
            print(user)
        else:
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com mesmo username')
            return redirect('/usuarios/cadastro')
        
        return redirect('/usuarios/logar')

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/empresarios/cadastrar_empresa') # Vai dar erro

        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
        return redirect('/usuarios/logar')
        
