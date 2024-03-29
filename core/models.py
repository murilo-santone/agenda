from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# Cria um novo evento pela página admin/ do django
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name="Data do evento")
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    #Formatação de data e hora para poder mostrar ao usuário
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y, às %H:%M')

    #Formatação de data e hora para manter a mesma data e hora na hora de editar o evento
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False