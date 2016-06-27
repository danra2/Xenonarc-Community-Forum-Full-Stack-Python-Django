from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
  class Meta:
      model = User
      fields = 'first_name', 'last_name', 'email', 'password'
# class RegisterForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=45)
#     last_name = forms.CharField(max_length=45)
#     email = forms.EmailField()
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(max_length=100, widget=forms.PasswordInput)

