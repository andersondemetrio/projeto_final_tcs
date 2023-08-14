from django.urls import path
from accounts.views import *
from django.contrib.auth import views as auth_views
 
urlpatterns = [        
    path('', login_view, name='login'),
    path('primeiro_acesso/', primeiro_acesso, name='primeiro_acesso'),
    path('recuperar_senha/', recuperar_senha, name='recuperar_senha'),
    path('accounts/login/', redirect_to_custom_login, name='custom_login_redirect'),
    path('logout/', logout_view, name='logout'),
    path('email_enviado/', enviar_email_cadastro, name='enviar_email_cadastro'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="recuperar_senha.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='email_recuperado.html'), name="password_reset_done"),
    path('redefinir_senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='redefinir_senha.html', 
        success_url='/redefinir_concluido/'), 
        name='password_reset_confirm'),
    path('redefinir_concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='redefinir_concluido.html'), name='password_reset_complete'),
    path('cadastro_usuario/',cadastro, name='cadastro_usuario'),
    path('cadastro_usuario_sucesso/', cadastro_usuario_sucesso, name='cadastro_usuario_sucesso'),
    # path('email_recuperado/', email_recuperado, name='email_recuperado'),
    # outras rotas do seu aplicativo aqui
    #teste
]
