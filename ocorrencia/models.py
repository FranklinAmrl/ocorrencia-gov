import uuid
from django.db import models
from stdimage.models import StdImageField
from mptt.models import MPTTModel
#from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser, BaseUserManager

from ocorrencia.consts import StatusUsuarioChoices, TipoUsuarioChoices

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)

    class Meta:
        abstract = True

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Ocorrencia(Base):
    CENTRO_CHOICES = (
        ('Almoxarifa-do-central', 'Almoxarifado Central'),
        ('Arquealogia', 'Arquealogia'),
        ('Apoio-pista-de-cooper', 'Apaio Pista de Cooper'),
        ('Biblioteca-central', 'Biblioteca Central'),
        ('Bloco-compartilhado-ccb', 'Bloco CoSSmpartilhado-CCB'),
        ('Bloco-compartilhados-outros', 'Bloco Compartilhado-CFCH/CE/CCSA'),
    )

    TIPO_OCORRENCIA_CHOICES = (
        ('Agressao', 'Agressão'),
        ('Roubo', 'Roubo'),
        ('Furto', 'Furto'),
    )

    TIPO_ENVOLVIDO_CHOICES = (
        ('Suspeito', 'Suspeito'),
        ('Vitima', 'Vitima'),
    )

    TIPO_GENERO_CHOICES = (
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outros', 'Outros'),
    )

    '''
    TIPO_OBJETO_CHOICES = (
        ('Feminino', 'Feminino'),
        ('Masculino', 'Masculino'),
        ('Outros', 'Outros'),
    )'''

    coordenadaX = models.CharField('Coordenadas X', max_length=255)
    coordenadaY = models.CharField('Coordenadas Y', max_length=255)
    centro = models.CharField('Centro', max_length=255, choices=CENTRO_CHOICES)
    referencia = models.CharField('Local de referência', max_length=255, null=True)
    data = models.DateTimeField('Data e hora', auto_now_add=False, auto_now=False)
    tipo = models.CharField('Tipo da ocorrência', max_length=255, choices=TIPO_OCORRENCIA_CHOICES)
    descricao = models.TextField('Descrição da ocorrência', max_length=255, null=True)
    envolvidoNome = models.CharField('Nome do envolvido', max_length=100, null=True, blank=True)
    tipoEnvolvido = models.CharField('Tipo do envolvido', max_length=255, choices=TIPO_ENVOLVIDO_CHOICES, null=True, blank=True)
    genero = models.CharField('Gênero do envolvido', max_length=255, choices=TIPO_GENERO_CHOICES, null=True, blank=True)
    cpf = models.IntegerField('CPF do envolvido', null=True, blank=True)
    email = models.EmailField('Email do envolvido', max_length=100, null=True, blank=True)
    fone = models.CharField('Telefone do envolvido', max_length=14, null=True, blank=True)
    imagem = StdImageField('Imagem', upload_to=get_file_path, null=True, blank=True)

    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

    def __str__(self):
        return self.tipo

class PassagemPlatao(Base):
    data = models.DateTimeField('Data e hora', auto_now_add=False, auto_now=False)
    descricao = models.TextField('Descrição da plantão', max_length=255, null=True)


    class Meta:
        verbose_name = 'Passagem de Plantão'
        verbose_name_plural = 'Passagens de Plantão'

    def __str__(self):
        return self.data


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, cpf, password, **extra_fields):
        if not cpf:
            raise ValueError('O email é obrigatório.')
        cpf = self.normalize_email(cpf)
        user = self.model(cpf=cpf, username=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    '''def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)'''

    def create_staffuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O usuário precisa de ter is_staff=True')

        return self._create_user(cpf, password, **extra_fields)

    def create_superuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O usuário precisa de ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O usuário precisa de ter is_staff=True')

        return self._create_user(cpf, password, **extra_fields)

class User(AbstractUser):
    status = models.PositiveSmallIntegerField(choices = StatusUsuarioChoices.choices, default=StatusUsuarioChoices.ATIVO)
    username = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('Email', unique=True)

    class Meta:
        ordering = ['first_name']

class Usuario(User,MPTTModel):
    fone = models.CharField('Telefone', max_length=15)
    perfil = models.PositiveSmallIntegerField(choices = TipoUsuarioChoices.choices)
    parent = models.ForeignKey('Usuario', null=True, blank=True, on_delete=models.PROTECT)
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            if self.perfil == TipoUsuarioChoices.ADMINISTRATOR:
                super().save(force_insert, force_update, using, update_fields)
            elif self.parent and self.perfil > self.parent.perfil:
                super().save(force_insert, force_update, using, update_fields)
        else:
            super().save(force_insert, force_update, using, update_fields)


    class MPTTMeta:
        order_insertion_by = ['first_name']

    def __str__(self):
        return f'Login do usuário: {self.cpf}'