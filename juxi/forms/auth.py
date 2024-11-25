

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )
    next = forms.CharField(
        widget=forms.HiddenInput,
    )


class LogoutForm(forms.Form):
    next = forms.CharField(
        widget=forms.HiddenInput,
    )
