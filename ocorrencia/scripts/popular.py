from ocorrencia.models import Usuario
from ocorrencia.consts import TipoUsuarioChoices
from django.contrib.auth.hashers import make_password
def run():
    usuario = Usuario.objects.create(username="11363683454",first_name="juan",last_name="ferreira",perfil=TipoUsuarioChoices.ADMINISTRATOR,email="teste1@email.com")
    usuario.password = make_password("senha@123")
    usuario.save()
