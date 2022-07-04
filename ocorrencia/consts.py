from django.db.models import IntegerChoices


class TipoUsuarioChoices(IntegerChoices):
    ADMINISTRATOR = 1, 'Administrador'
    GESTOR = 2, 'Gestor'
    INSPETOR = 3, 'Inspetor'
    NOTIFICANTE = 4, 'Notificante'

class StatusUsuarioChoices(IntegerChoices):
    ATIVO = 1, 'Ativo'
    INATIVO = 2, 'Inativo'
    NOT_VERIFIED = 3, 'Não Verificado'

class TipoOcorrenciaChoices(IntegerChoices):
    AGRESSAO = 1, 'Agressão'
    FURTO = 2, 'Furto'
    ROUBO = 3, 'Roubo'

class TipoGeneroChoices(IntegerChoices):
    FEMININO = 1, 'Feminino'
    MASCULINO = 2, 'Masculino'
    OUTROS = 3, 'Outros'

class TipoCentroChoices(IntegerChoices):
    BIBLIOTECA_GENTAL = 1, 'Biblioteca Central'
    CIN = 2, 'CIn'
    SSI = 3, 'SSI'


class TipoEnvolvidoChoices(IntegerChoices):
    SUSPEITO = 1, 'Suspeito'
    VITIMA = 2, 'Vitima'