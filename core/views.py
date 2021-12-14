#redirect - direciona pagina padrão para /agenda/
from django.shortcuts import render, redirect
from core.models import Evento
#======================================================================================
#login_required - permite acessar página somente se estiver conectado
from django.contrib.auth.decorators import login_required
#=======================================================================================
#authenticate, login - usado para autenticar e logar
#logout - limpa sessão de login
from django.contrib.auth import authenticate, login, logout
#========================================================================================
from django.contrib import messages
# Create your views here.

#redirect - direciona página principal para /agenda/
#Método 1
#def index(request):
#    return redirect('/agenda/')
# Método 2 de direcionamento não precisa passar por uma view, para ver entre na urls.py
#========================================================================================#
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        #recuperando o username/password para validação
        username = request.POST.get('username')
        password = request.POST.get('password')
        #validação de autenção
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            #fazendo login caso usuário não seja none(vazio)
            login(request, usuario)
            return redirect('/')
        else:
            #tratativa de erro caso usuario ou senha inválido
            messages.error(request, "Usuário ou senha inválido.")
            return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    #Buscando o primeiro evento cadastrado na lista;
    #evento = Evento.objects.get(id=1)

    #Buscando todos os eventos (será criado uma lista de todos os eventos);
    #eventos = Evento.objects.all()

    #user logado
    usuario = request.user
    #Buscando eventos por usuário logado
    eventos = Evento.objects.filter(usuario=usuario)

    #dicionário com os dados dos eventos;
    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    print(id_evento)
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            #metodo 2
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
                # update na tabela, metodo 1
                # Evento.objects.filter(id=id_evento).update(titulo=titulo,
                #                                           data_evento=data_evento,
                #                                           descricao=descricao)
        else:
            #novo evento pela página html criada
            Evento.objects.create(titulo=titulo,
                                  data_evento= data_evento,
                                  descricao= descricao,
                                  usuario= usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')