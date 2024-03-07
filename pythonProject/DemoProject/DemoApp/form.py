from django import forms
from .models import User, Login, alogin

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model = alogin
        fields = "__all__"

