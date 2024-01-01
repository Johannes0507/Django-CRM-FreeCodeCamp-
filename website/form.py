from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    # 使用bootstrap的form類型所以另外插入form的class與placeholder屬性 
    email = forms.EmailField(label="", 
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    first_name = forms.CharField(label="", 
                                 max_length=100, 
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓氏'}))
                                 
    last_name = forms.CharField(label="", 
                                max_length=100, 
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名字'}))
    
    class Meta:
        model = User
        filds = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2') 