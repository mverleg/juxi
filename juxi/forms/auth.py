
from django import forms

from juxi.views.util import INPUT_CLASSES, ERROR_CLASSES


class LoginForm(forms.Form):
    error_css_class = ERROR_CLASSES

    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={
            'tabindex': 1,
            'placeholder': "h4ck3r",
            'class': INPUT_CLASSES,
        }),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'tabindex': 2,
            'placeholder': "s3cr3t",
            'class': INPUT_CLASSES,
        }),
    )
    next = forms.CharField(
        widget=forms.HiddenInput,
    )


class LogoutForm(forms.Form):
    error_css_class = ERROR_CLASSES

    next = forms.CharField(
        widget=forms.HiddenInput,
    )
