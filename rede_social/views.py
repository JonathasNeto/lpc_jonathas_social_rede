from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil,Publicao,Comentario


@login_required(login_url='/login/')
def index(request):
    
    return render(request,'index.html')


def login_user(request):
    return render(request,'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Usuario e senha Invalido ")
    return redirect('/login/')


def logout_user(request):
    logout(request)
    return redirect('/login')


def todos(request):
    todos = Publicao.objects.filter(ativo=True)
   
    return render(request,'todos.html',{'todos':todos})

def publicar(request):
    pub = Perfil.objects.filter(ativo=True)
    print(pub)
    return render(request,'publicar.html',{'pub':pub})

def comentarios(request):
    coment=Comentario.objects.filter(ativo=True)
    return render(request,'comentarios.html',{'coment':coment})

def amigos(request):
    perfil=Perfil.objects.filter(ativo=True)
    print(perfil.values)
    return render(request,'amigos.html',{'perfil':perfil})