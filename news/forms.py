from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import News, Comment

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username:', required=True, widget=forms.TextInput(attrs={'class': 'input mb-2', 'placeholder':'Логин'}))
    password1 = forms.CharField(label='Password:', required=True, widget=forms.PasswordInput(attrs={'class': 'input mb-2', 'placeholder':'Парол'}))
    password2 = forms.CharField(label='Confirm Password:', required=True, widget=forms.PasswordInput(attrs={'class': 'input mb-2', 'placeholder':'Паролни тасдиқлаш'}))
    email = forms.EmailField(label='Email:', required=True, widget=forms.TextInput(attrs={'class': 'input mb-2', 'placeholder':'Email'}))
    first_name = forms.CharField(label='Name:', required=True, widget=forms.TextInput(attrs={'class': 'input mb-2', 'placeholder':'Исм'}))
    last_name = forms.CharField(label='Surname:', required=True, widget=forms.TextInput(attrs={'class': 'input mb-2', 'placeholder':'Фамилия'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            return user

            
      