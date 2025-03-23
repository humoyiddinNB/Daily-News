from .models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError('Parollar mos emas')
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Foydalanuvchi nomi'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Parol'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise ValidationError('Bunday foydalanuvchi nomi mavjud emas.')
        return username

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

