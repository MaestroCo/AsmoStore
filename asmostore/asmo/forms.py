from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import ProductReview, ShippingAddress, UserProfile, BlogReview


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['comment', 'rating']


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'district', 'zipcode', 'mobile', 'email']
        labels = {
            'address': 'Manzil',
            'city': 'Shahar',
            'district': 'Tuman',
            'zipcode': 'Pochta kodi',
            'mobile': 'Mobil raqami',
            'email': 'Email manzili',
        }
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manzilingizni kiriting'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Shaharingizni kiriting'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tumaningizni kiriting'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pochta kodini kiriting'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobil raqamingizni kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email manzilingizni kiriting'}),
        }


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ism'
    }))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Familiya'
    }))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ucername'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parol'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni takrorlang'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'style': 'margin-top: 10px'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'style': 'margin-top: 10px'
    }))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'first_name', 'last_name', 'phone', 'telegram']
        labels = {
            'photo': 'Rasm',
            'address': 'Manzil',
            'phone': 'Telefon',
            'telegram': 'Telegram',
            'first_name': 'Ism',
            'last_name': 'Familiya'
        }

        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rasim',
                'style': 'margin-top: 10px'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqam',
                'style': 'margin-top: 10px'
            }),
            'telegram': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://t.me/nickname',
                'style': 'margin-top: 10px'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Isim',
                'style': 'margin-top: 10px'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Familiya',
                'style': 'margin-top: 10px'
            })
        }


class BlogReviewForm(forms.ModelForm):
    class Meta:
        model = BlogReview
        fields = ['comment']