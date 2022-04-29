from ast import Pass
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Ocorrencia, PassagemPlatao, CustomUsuario

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'centro', 'tipo', 'criado', 'modificado')

@admin.register(PassagemPlatao)
class PassagemPlantaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'descricao', 'criado', 'modificado')

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
    )