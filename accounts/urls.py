from django.urls import path
from accounts.views import *
urlpatterns = [        
    path('login/', login_view, name='login'),
    path('primeiro_acesso/', primeiro_acesso, name='primeiro_acesso'),
    path('recuperar_senha/', recuperar_senha, name='recuperar_senha'),
    path('accounts/login/', redirect_to_custom_login, name='custom_login_redirect'),
    path('logout/', logout_view, name='logout'),
    path('pagina_email_enviado/', enviar_email_cadastro, name='enviar_email_cadastro'),
    # outras rotas do seu aplicativo aqui
]