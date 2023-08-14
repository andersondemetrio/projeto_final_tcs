from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

#autenticação customizável para poder logar com cpf ou matricula

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Verifica o usuário no banco para verificar se o username corresponde a um cpf ou matricula no model Colaboradores
        # Se encontrado um usuário, verifica se a senha corresponde a senha do usuário encontrado
        try:
            user = UserModel._default_manager.get(Q(username=username) | Q(colaboradores__cpf=username) | Q(colaboradores__matricula=username))
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    # Obtem o usuário baseado em seu id
    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel._default_manager.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
