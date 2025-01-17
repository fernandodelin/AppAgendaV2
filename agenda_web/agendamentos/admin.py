from django.contrib import admin # type: ignore
from .models import Cliente, Servico, Profissional, Agendamento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'data_cadastro')
    search_fields = ('nome', 'telefone', 'email')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'preco')
    search_fields = ('nome',)

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefone')
    search_fields = ('usuario__username', 'usuario__first_name', 'telefone')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'profissional', 'data_hora', 'status')
    list_filter = ('status', 'data_hora', 'profissional')
    search_fields = ('cliente__nome', 'servico__nome', 'profissional__usuario__first_name')
# Register your models here.
