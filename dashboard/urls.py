from django.urls import path
from dashboard.views import *
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('inserir_gasto_fixo/', inserir_gasto_fixo, name='inserir_gasto_fixo'),
    path('inserir_mao_de_obra/', inserir_mao_de_obra, name='inserir_mao_de_obra'),
    path('cargos_vieww/', cargos_vieww, name='cargos_vieww'),
    path('listar_enderecos/', endereco_view, name='endereco_view'),
    path('inserir_empresa/', inserir_empresa, name='inserir_empresa'),
    path('inserir_endereco/', inserir_endereco, name='inserir_endereco'),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
    path('inserir_cargo/', inserir_cargo, name='inserir_cargo'),
    path('editar_cargo/', editar_cargo, name='editar_cargo'),
    path('deletar_cargo/<int:cargo_id>/', deletar_cargo, name='deletar_cargo'),
    path('inserir_beneficio/', inserir_beneficio, name='inserir_beneficio'),
    path('inserir_encargo/', inserir_encargo, name='inserir_encargo'),
    path('inserir_data/', inserir_data, name='inserir_data'),
    path('inserir_jornada/', inserir_jornada, name='inserir_jornada'),
    path('inserir_horas/', inserir_horas, name='inserir_horas'),
    path('inserir_calendario/',inserir_calendario,name='inserir_calendario'),
    path('colaboradores_view/',colaboradores_view,name='colaboradores_view'),
    path('busca/', search, name='busca'),
]