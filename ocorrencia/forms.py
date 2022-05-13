from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario

class UsuarioCreateForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = '__all__'
        labels = {'username': 'Username/Email'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
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