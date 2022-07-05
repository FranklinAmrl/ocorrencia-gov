from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Management, Ocorrencia, PassagemPlatao, User

from .forms import CreateManagementUserForm

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'centro', 'tipo', 'criado', 'modificado')

@admin.register(PassagemPlatao)
class PassagemPlantaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'descricao', 'criado', 'modificado')

@admin.register(User)
class UsuarioAdmin(UserAdmin):
    add_form = CreateManagementUserForm
    model = User
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    fieldsets = (
        (None, {'fields': ('cpf', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('date_joined', 'last_login')}),
    )