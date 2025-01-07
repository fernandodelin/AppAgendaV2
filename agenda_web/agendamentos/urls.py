from django.urls import path
from . import views

urlpatterns = [
   path('', views.dashboard, name='dashboard'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    path('agendamentos/novo/', views.criar_agendamento, name='criar_agendamento'),
    path('agendamentos/<int:pk>/', views.detalhe_agendamento, name='detalhe_agendamento'),
    path('agendamentos/<int:pk>/editar/', views.editar_agendamento, name='editar_agendamento'),
]
