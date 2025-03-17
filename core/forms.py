from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    #Ocultamos el texto del password 
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data

    def save(self):
        user = super().save(commit=True)  # Guarda el usuario en BD
        user.set_password(self.cleaned_data["password"])  # Encripta la contraseña
        user.save()  # Guarda en la BD si commit es True
        return user
    

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
