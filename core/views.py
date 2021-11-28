#redirect - direciona pagina padrão para /agenda/
from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

#redirect - direciona página principal para /agenda/
#Método 1
#def index(request):
#    return redirect('/agenda/')
# Método 2 de direcionamento não precisa passar por uma view, para ver entre na urls.py


def lista_eventos(request):
    #Buscando o primeiro evento cadastrado na lista;
    #evento = Evento.objects.get(id=1)

    #Buscando todos os eventos (será criado uma lista de todos os eventos);
    eventos = Evento.objects.all()

    #dicionário com os dados dos eventos;
    dados = {'eventos': eventos}
    return render(request, 'agenda.html', dados)

