from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
import re

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={'invalid': 'Email inválido: por favor digite um email válido'}
    )
    foto = forms.ImageField(required=True)

    class Meta:
        model = Usuario
        fields = ['foto', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 6 or not re.search(r"[^\w\s]", password):
            raise forms.ValidationError("Senha fraca: mínimo 6 caracteres incluindo 1 especial.")
        return password
