from django import forms
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class BookCreateForm(forms.Form):
#     book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'myclass'}))
#     author=forms.CharField(widget=forms.TextInput(attrs={'class':'myclass'}))
#     price=forms.IntegerField(widget=forms.TextInput(attrs={'class':'myclass'}))
#     pages=forms.IntegerField(widget=forms.TextInput(attrs={'class':'myclass'}))

    #django modelform
class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        # fields=["bookname","author","price","pages"]

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

