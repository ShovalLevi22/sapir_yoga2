from django import forms
from landing_page.models import UserInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

        labels = {
            'username':'הכנס שם מלא:',
            'email':'הכנס כתובת מייל',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': "textinputclass"}),
            # 'last_name': forms.Textarea(attrs={'class': 'textinputclass'}),
            # 'phone': forms.Textarea(attrs={'class': 'textinputclass'}),
            'email': forms.TextInput(attrs={'class': "textinputclass"}),
        }

class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('phone',)
        labels = {
            'phone': 'הכנס טלפון',
            }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'textinputclass'}),
        }
