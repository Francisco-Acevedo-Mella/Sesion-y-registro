from django import forms
from django.db.models import fields
from app.models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username',  'role','password', 'nacimiento', 'email']
        labels = {
            'name': 'Nombre',
            'username': 'Tu Usuario',
            'role': 'Rol',
            'password': 'Contraseña',
            'nacimiento' : 'Nacimiento',
            'email' : 'email',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(choices=User.OPCIONES_ROL, attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'Nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Tu Usuario',
            'password': 'Contraseña',
        }
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
