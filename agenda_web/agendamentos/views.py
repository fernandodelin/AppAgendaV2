from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Agendamento
from .forms import AgendamentoForm
from datetime import datetime, timedelta



@login_required
def dashboard(request):
    hoje = datetime.now()
    agendamentos_hoje = Agendamento.objects.filter(
        data_hora__date=hoje.date()
    ).order_by('data_hora')
    proximos_agendamentos = Agendamento.objects.filter(
        data_hora__date__gt=hoje.date()
    ).order_by('data_hora')[:5]
    
    return render(request, 'agendamentos/dashboard.html', {
        'agendamentos_hoje': agendamentos_hoje,
        'proximos_agendamentos': proximos_agendamentos
    })

@login_required
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('-data_hora')
    return render(request, 'agendamentos/lista_agendamentos.html', {
        'agendamentos': agendamentos
    })

@login_required
def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save()
            messages.success(request, 'Agendamento criado com sucesso!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    
    return render(request, 'agendamentos/form_agendamento.html', {
        'form': form,
        'titulo': 'Novo Agendamento'
    })

@login_required
def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agendamento atualizado com sucesso!')
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm(instance=agendamento)
    
    return render(request, 'agendamentos/form_agendamento.html', {
        'form': form,
        'titulo': 'Editar Agendamento'
    })

@login_required
def detalhe_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    return render(request, 'agendamentos/detalhe_agendamento.html', {
        'agendamento': agendamento
    })