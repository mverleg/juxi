

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'h4ck3r'}),
        label="Username"
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label="Password"
    )
    next = forms.CharField(
        widget=forms.HiddenInput,
    )


class LogoutForm(forms.Form):
    next = forms.CharField(
        widget=forms.HiddenInput,
    )
