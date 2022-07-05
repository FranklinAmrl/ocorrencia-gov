from ocorrencia.models import User
from ocorrencia.consts import ManagementTypeChoices
from django.contrib.auth.hashers import make_password
def run():
    usuario = User.objects.create(username="11363683454",first_name="juan",last_name="ferreira",perfil=ManagementTypeChoices.ADMINISTRATOR,email="teste1@email.com")
    usuario.password = make_password("senha@123")
    usuario.save()
