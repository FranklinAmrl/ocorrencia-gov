from django.db.models import IntegerChoices

def list_choices(cls) -> list:
        return [t[0] for t in cls.choices]

def dict_choices(cls) -> dict:
        return dict(cls.choices)

class ManagementTypeChoices(IntegerChoices):
    ADMINISTRATOR = 1, 'Administrador'
    GESTOR = 2, 'Gestor'
    INSPETOR = 3, 'Inspetor'
    NOTIFICANTE = 4, 'Notificante'

class StatusUsuarioChoices(IntegerChoices):
    ATIVO = 1, 'Ativo'
    INATIVO = 2, 'Inativo'
    NOT_VERIFIED = 3, 'Não Verificado'

class GenreChoices(IntegerChoices):
    MALE = 1, 'Masculino'
    FEMININE = 2, 'Feminino'
    OTHERS = 3, 'Outros'
    NOT_INFORM = 4, 'Não Informar'

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


MONTHLIST = ['', 'jan', 'fev', 'mar', 'abr', 'maio', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']