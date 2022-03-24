from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')

class updateform(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'mobile')

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address', 'state', 'mobile_no', 'zipcode')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'