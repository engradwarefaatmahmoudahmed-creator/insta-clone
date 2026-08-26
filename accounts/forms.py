from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password'
    )

    password_confirmation = forms.CharField(
        widget=forms.PasswordInput,
        label='Password confirmation'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'profile_picture',
            'bio',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'User with this Email already exists.'
            )

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get(
            'password_confirmation'
        )

        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError(
                    'Passwords do not match.'
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username'
    )

    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password'
    )


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
            'profile_picture',
            'bio',
        ]