from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email', 'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username', 'required': 'required'}),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Password', 'required': 'required'}),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirm Password', 'required': 'required'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'required': 'required'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'required': 'required'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password', 'required': 'required'})



