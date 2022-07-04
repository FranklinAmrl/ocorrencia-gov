
from ocorrencia.models import User, Usuario
from ocorrencia.consts import TipoUsuarioChoices

def get_descendants_users(user,notificante_filter=False):
    logged_user = Usuario.objects.filter(user_ptr = user).first()
    if logged_user:
        users = logged_user.get_descendants()
    elif not User.objects.filter(user_ptr = user).exists():
        users = Usuario.objects.all()
    else:
        users = Usuario.objects.none()
    if notificante_filter:
        users = users.filter(perfil = TipoUsuarioChoices.NOTIFICANTE)
    return users