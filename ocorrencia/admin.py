from ast import Pass
from django.contrib import admin

from .models import Ocorrencia, PassagemPlatao

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'centro', 'tipo', 'criado', 'modificado')

@admin.register(PassagemPlatao)
class PassagemPlantaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'descricao', 'criado', 'modificado')