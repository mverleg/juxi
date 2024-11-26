

from django import forms

from juxi.views.util import INPUT_CLASSES


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': "h4ck3r",
            'class': INPUT_CLASSES,
        }),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': "s3cr3t",
            'class': INPUT_CLASSES,
        }),
    )
    next = forms.CharField(
        widget=forms.HiddenInput,
    )


class LogoutForm(forms.Form):
    next = forms.CharField(
        widget=forms.HiddenInput,
    )
