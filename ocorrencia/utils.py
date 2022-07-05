
from ocorrencia.models import Management, User
from ocorrencia.consts import ManagementTypeChoices

def get_descendants_users(user,NOTIFICANTE_filter=False):
    logged_user = Management.objects.filter(user_ptr = user).first()
    if logged_user:
        users = logged_user.get_descendants()
    elif not User.objects.filter(user_ptr = user).exists():
        users = Management.objects.all()
    else:
        users = Management.objects.none()
    if NOTIFICANTE_filter:
        users = users.filter(office = ManagementTypeChoices.NOTIFICANTE)
    return users

def get_not_NOTIFICANTE_descendants(user):
    logged_user = Management.objects.filter(user_ptr = user).first()
    if logged_user:
        users = logged_user.get_descendants().exclude(office = ManagementTypeChoices.NOTIFICANTE )
    elif not User.objects.filter(user_ptr = user).exists():
        users = Management.objects.all().exclude(office= ManagementTypeChoices.NOTIFICANTE)
    else:
        users = Management.objects.none()
    return users
