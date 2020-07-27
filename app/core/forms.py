from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'birthday', 'programming_exp', 'avatar', 'education',
                  'phone')


class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
