from django import forms
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    username=  forms.CharField(max_length=30,label="İstifadəçi adı:")
    password = forms.CharField(max_length=40,label="Şifrə:",widget=PasswordInput)
    


class RegisterForm(forms.Form):
    username = CharField(max_length=20,label="İstifadəçi adı:")
    password = CharField(max_length=25,label="Şifrə",widget=forms.PasswordInput)
    confirm  = CharField(max_length=25,label="Şifrəni təkrarlayın:",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if confirm and password and password != confirm:
            raise forms.ValidationError("Şifrələr eyni deyil.")
    
        values = {
            "username": username,
            "password": password
        }
