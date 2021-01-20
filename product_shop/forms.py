from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import GetInTouch, Checkout, ProductOrder

class GetInTouchForm(forms.ModelForm):

    class Meta:
        model = GetInTouch
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name', 'data-error':'Please enter your name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email', 'data-error':'Please enter your email'}),
            'subject' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Subject', 'data-error':'Please enter your subject'}),
            'text' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Text', 'data-error':'Please enter your Text'}),
        }

class UserReg(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username', 'data-error':'Please enter your username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password', 'data-error':'Password is incorrect'}))
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password', 'data-error':'Invalid Input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email', 'data-error':'This must be email, not another'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class UserLog(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Username', 'data-error':'Error'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Your Password', 'data-error':'Passwort incorrect or invalid'}))

class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Checkout
        fields = '__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'adress':forms.TextInput(attrs={'class':'form-control'})
        }
