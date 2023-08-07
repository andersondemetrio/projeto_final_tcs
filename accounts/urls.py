from django.urls import path
from accounts.views import *
urlpatterns = [
    path('landing_page/', landing_page_view, name='landing_page'),
    path('', login_view, name='login'),
    path('primeiro_acesso/', primeiro_acesso, name='primeiro_acesso'),
    path('recuperar_senha/', recuperar_senha, name='recuperar_senha'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
     path('pagina_email_enviado/', enviar_email_cadastro, name='enviar_email_cadastro'),
    # outras rotas do seu aplicativo aqui
]