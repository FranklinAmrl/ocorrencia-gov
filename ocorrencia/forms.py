from dataclasses import fields
from django import forms
from django.contrib.auth.hashers import make_password

from django.contrib.auth.forms import UserCreationForm

from ocorrencia.consts import TipoCentroChoices, TipoOcorrenciaChoices

from .models import Management, Ocorrencia

class CreateManagementUserForm(forms.ModelForm):
    

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password','Senhas Não Condizem!')
        else:
            password = self.cleaned_data.get('password')
            if password:
                self.cleaned_data['password'] =  make_password(password)
            else:
                self.add_error('password','Campo obrigatório!')
        return super().clean()

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir Senha",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Management
        fields = ['username','first_name', 'email','office','parent', 'password', 'password2']
        
        widgets = {
            'username':forms.TextInput(
                    attrs={
                        "placeholder": "Login",
                        "class": "form-control"
                    }),
            'first_name':forms.TextInput(
                    attrs={
                        "placeholder": "Nome",
                        "class": "form-control"
                    }),
            'email':forms.EmailInput(
                    attrs={
                        "placeholder": "Email",
                        "class": "form-control",
                    }),
            'office':forms.Select(
                    attrs={
                        "class": "form-control",
                    }),
            'parent':forms.Select(
                    attrs={
                        "class": "form-control",
                    }),
            'password':forms.PasswordInput(
                attrs={
                    "placeholder": "Senha",
                    "class": "form-control"
                })
        }


class LoginUsuarioForm(forms.Form):
    username = forms.CharField()
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

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome de Usuário",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Management
        fields = ('username', 'email', 'password1', 'password2')