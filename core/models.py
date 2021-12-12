from django.db import models
from django.contrib.auth.models import User

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

    #Formatação de data e hora para padrão BR
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y, às %H:%M')