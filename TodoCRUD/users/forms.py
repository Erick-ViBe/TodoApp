from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django.contrib.auth import authenticate

class UserForm(forms.Form):
    usuario = forms.CharField(max_length=25)
    contraseña = forms.CharField(max_length=25, widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('usuario')
        password = self.cleaned_data['contraseña']
        user_username = User.objects.filter(username=username).exists()
        user = authenticate(username=username, password=password)
        if not user:
            if user_username:
                raise forms.ValidationError('La contraseña es incorrecta bbe')
            else:
                raise forms.ValidationError('El usuario no existe!!!')
        return self.cleaned_data
