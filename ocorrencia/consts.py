from django.db.models import IntegerChoices


class TipoUsuarioChoices(IntegerChoices):
    ADMINISTRATOR = 1, 'Administrador'
    GESTOR = 2, 'Gestor'
    INSPETOR = 3, 'Inspetor'
    NOTIFICANTE = 4, 'Notificante'