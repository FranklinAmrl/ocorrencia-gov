import uuid
from django.db import models
from stdimage.models import StdImageField
from mptt.models import MPTTModel
#from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser, BaseUserManager

from ocorrencia.consts import StatusUsuarioChoices, TipoCentroChoices, TipoEnvolvidoChoices, TipoGeneroChoices, TipoUsuarioChoices, TipoOcorrenciaChoices

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

    local = models.CharField('Local da ocorrência', max_length=255)
    coordenadaX = models.CharField('Coordenadas X', max_length=255, null=True, blank=True)
    coordenadaY = models.CharField('Coordenadas Y', max_length=255, null=True, blank=True)
    centro = models.PositiveSmallIntegerField(choices = TipoCentroChoices.choices)
    referencia = models.CharField('Local de referência', max_length=255, null=True)
    data = models.DateTimeField('Data e hora', auto_now_add=False, auto_now=False)
    tipo = models.PositiveSmallIntegerField(choices = TipoOcorrenciaChoices.choices)
    descricao = models.TextField('Descrição da ocorrência', max_length=255, null=True)
    envolvidoNome = models.CharField('Nome do envolvido', max_length=100, null=True, blank=True)
    envolvidos = models.PositiveSmallIntegerField(choices = TipoEnvolvidoChoices.choices, null=True, blank=True)
    genero = models.PositiveSmallIntegerField(choices = TipoGeneroChoices.choices, null=True, blank=True)
    cpf = models.IntegerField('CPF do envolvido', null=True, blank=True)
    email = models.EmailField('Email do envolvido', max_length=100, null=True, blank=True)
    fone = models.CharField('Telefone do envolvido', max_length=14, null=True, blank=True)
    imagem = StdImageField('Imagem', upload_to=get_file_path, null=True, blank=True)

    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

    def __str__(self):
        return self.tipo

    @classmethod
    def get_qtd_tipo_ocorrencia(cls):

        save_data = {}
        index_numero_tipo = 0
        descricao_tipo = 1
        qtd = 0
        tipos = TipoOcorrenciaChoices.choices
        for tipo in tipos:
            qtd = cls.objects.filter(tipo=tipo[index_numero_tipo]).count()
            save_data[tipo[descricao_tipo]] = qtd

        return save_data


class PassagemPlatao(Base):
    data = models.DateTimeField('Data e hora', auto_now_add=False, auto_now=False)
    descricao = models.TextField('Descrição da plantão', max_length=255, null=True)


    class Meta:
        verbose_name = 'Passagem de Plantão'
        verbose_name_plural = 'Passagens de Plantão'

    def __str__(self):
        return self.data


# class UsuarioManager(BaseUserManager):

#     use_in_migrations = True

#     def _create_user(self, cpf, password, **extra_fields):
#         if not cpf:
#             raise ValueError('O email é obrigatório.')
#         cpf = self.normalize_email(cpf)
#         user = self.model(cpf=cpf, username=cpf, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     '''def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)

#         return self._create_user(email, password, **extra_fields)'''

#     def create_staffuser(self, cpf, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', False)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('O usuário precisa de ter is_staff=True')

#         return self._create_user(cpf, password, **extra_fields)

#     def create_superuser(self, cpf, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('O usuário precisa de ter is_superuser=True')

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('O usuário precisa de ter is_staff=True')

#         return self._create_user(cpf, password, **extra_fields)

class User(AbstractUser):
    status = models.PositiveSmallIntegerField(choices = StatusUsuarioChoices.choices, default=StatusUsuarioChoices.NOT_VERIFIED)
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