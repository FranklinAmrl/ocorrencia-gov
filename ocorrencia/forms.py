from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ocorrencia.consts import TipoOcorrenciaChoices

from .models import Usuario
class UsuarioCreateForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {'username': 'Username/CPF'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.cpf = self.cleaned_data['username']
        if commit:
            user.save()
        return user

class UsuarioChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = '__all__'


class LoginUsuarioForm(forms.Form):
    username = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput())

class FiltroRelatorioOcorrencia(forms.Form):
    
    tipo = forms.ChoiceField(choices=TipoOcorrenciaChoices.choices+[('','Todxs os tipos de ocorrência')], 
    required=False, 
    widget=forms.Select(
        attrs={'class': 'form-control'

    }))

    data_inicial = forms.DateField( 
    required=True, 
    widget=forms.DateInput(
        attrs={'class': 'form-control',
                'type':"date"

    }))

    data_final = forms.DateField(
    required=True, 
    widget=forms.DateInput(
        attrs={'class': 'form-control',
                'type':"date"

    }))
