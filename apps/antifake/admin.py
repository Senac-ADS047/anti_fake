from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Sala, AulaSemanal, Tarefa

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    fieldsets = UserAdmin.fieldsets + (
        ("Informações adicionais", {'fields': ('foto', 'codigo_verificacao', 'email_verificado')}),
    )
    list_display = ('username', 'email', 'email_verificado', 'is_staff')
    search_fields = ('username', 'email')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descricao')
    search_fields = ('numero',)

@admin.register(AulaSemanal)
class AulaSemanalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia_semana', 'hora_inicio', 'hora_fim', 'sala')
    list_filter = ('dia_semana', 'sala')
    search_fields = ('nome',)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'hora', 'aula', 'criado_por')
    list_filter = ('data',)
    search_fields = ('nome', 'descricao')


