import uuid
from django.db import models
from stdimage.models import StdImageField
from mptt.models import MPTTModel

from django.contrib.auth.models import AbstractUser

from ocorrencia.consts import GenreChoices, ManagementTypeChoices, StatusUsuarioChoices, TipoCentroChoices, TipoEnvolvidoChoices, TipoGeneroChoices, ManagementTypeChoices, TipoOcorrenciaChoices

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
class User(AbstractUser):

    token_reset_password = models.CharField(max_length=200, blank=True, null=True)
    token_data = models.DateTimeField(blank=True ,null=True)
    status = models.PositiveSmallIntegerField(choices = StatusUsuarioChoices.choices, default=StatusUsuarioChoices.NOT_VERIFIED)
    #genre = models.PositiveSmallIntegerField(choices=GenreChoices.choices)
    #profile_picture = models.ImageField(null=True, blank=True, upload_to=get_file_path)
    class Meta:
        ordering = ['first_name']
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Management(User,MPTTModel):

    parent = models.ForeignKey('Management', null=True, blank=True, on_delete=models.PROTECT)
    office = models.PositiveSmallIntegerField(choices = ManagementTypeChoices.choices)
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            if self.perfil == ManagementTypeChoices.ADMINISTRATOR:
                super().save(force_insert, force_update, using, update_fields)
            elif self.parent and self.perfil > self.parent.perfil:
                super().save(force_insert, force_update, using, update_fields)
        else:
            super().save(force_insert, force_update, using, update_fields)

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    # ## todo usuário Mangement será ativo na criação ##
    # self.status = StatusUserChoices.ACTIVE
    # return super().save(force_insert, force_update, using, update_fields)

    class MPTTMeta:
        order_insertion_by = ['first_name']