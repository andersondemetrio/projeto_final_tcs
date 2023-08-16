from django.urls import path
from dashboard.views import *
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('inserir_gasto_fixo/', inserir_gasto_fixo, name='inserir_gasto_fixo'),
    path('inserir_mao_de_obra/', inserir_mao_de_obra, name='inserir_mao_de_obra'),
    path('cargos_vieww/', cargos_vieww, name='cargos_vieww'),
    path('listar_enderecos/', endereco_view, name='endereco_view'),
    path('inserir_empresa/', inserir_empresa, name='inserir_empresa'),

]