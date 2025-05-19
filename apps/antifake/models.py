from django.db import models
from django.contrib.auth.models import AbstractUser
import os




def caminho_foto_usuario(instance, filename):
    # Cria a pasta com o nome do username
    return os.path.join('usuarios', instance.username, filename)

# Modelo de usuário personalizado
class Usuario(AbstractUser):
    foto = models.ImageField(upload_to=caminho_foto_usuario, blank=True, null=True)
    codigo_verificacao = models.CharField(max_length=6, blank=True, null=True)
    email_verificado = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Modelo de sala de aula
class Sala(models.Model):
    numero = models.CharField(max_length=10)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Sala {self.numero}"


# Modelo de aulas recorrentes semanais
class AulaSemanal(models.Model):
    DIAS_SEMANA = [
        (0, 'Segunda-feira'),
        (1, 'Terça-feira'),
        (2, 'Quarta-feira'),
        (3, 'Quinta-feira'),
        (4, 'Sexta-feira'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    ]

    nome = models.CharField(max_length=100)
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    sala = models.ForeignKey(Sala, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Aula semanal"
        verbose_name_plural = "Aulas semanais"

    def __str__(self):
        return f"{self.nome} - {self.get_dia_semana_display()} ({self.hora_inicio} às {self.hora_fim})"


# Tarefa associada a um dia específico, e opcionalmente a uma aula
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    hora = models.TimeField()
    aula = models.ForeignKey(AulaSemanal, on_delete=models.SET_NULL, null=True, blank=True)
    criado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.data}"
