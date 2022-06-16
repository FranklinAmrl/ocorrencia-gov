from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ocorrencia.consts import TipoCentroChoices, TipoOcorrenciaChoices

from .models import Ocorrencia, Usuario
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
    
    tipo = forms.ChoiceField(choices=TipoOcorrenciaChoices.choices+[('','Todos os tipos de ocorrência')], 
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
class CreateOcorrenciaForm(forms.ModelForm):

    centro = forms.ChoiceField(choices = TipoCentroChoices.choices+[('','Selecione')], 
    widget=forms.Select(
        attrs={'class': 'form-control'

    }))
    tipo = forms.ChoiceField(choices=TipoOcorrenciaChoices.choices+[('','Selecione')],
    widget=forms.Select(
        attrs={'class': 'form-control'

    }))
    data = forms.DateField( 
    required=True, 
    widget=forms.DateInput(
        attrs={'class': 'form-control',
                'type':"date"

    }))

    class Meta():
        
        model = Ocorrencia
        fields = ('local', 'coordenadaX', 'coordenadaY', 'centro', 'referencia', 'tipo', 'data', 'descricao')


        widgets = {
            'local' : forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'coordenadaX' : forms.TextInput(
                attrs={'class': 'form-control'})
            ,
            'coordenadaY' : forms.TextInput(
                attrs={'class': 'form-control'}
            ),
                        
            'referencia' : forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'descricao' : forms.Textarea(
                attrs={'class': 'form-control'})
        }


