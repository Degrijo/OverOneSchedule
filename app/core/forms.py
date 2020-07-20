from django import forms
from django.contrib.auth import get_user_model


class SignUpForm(forms.Form):
    password1 = forms.CharField(min_length=8, max_length=20)
    password2 = forms.CharField(min_length=8, max_length=20)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(
                "Passwords should be same",
            )
        return password2

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2'
        )
