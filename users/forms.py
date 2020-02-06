from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Services, Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ServiceUpdateForm(ModelForm):
    class Meta:
        model = Services
        fields = ['activation']


class ServiceForm(ModelForm):
    class Meta:
        model = Services
        fields = ['activation']

    def user_service(self):
        return self.user.activation


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']


class CommentUpdateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['message']



