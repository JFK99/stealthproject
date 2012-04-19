from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth import models
from models import idea


class ideaForm(forms.Form):
    description = forms.CharField(
    	max_length=1000, 
    	label='',
    	widget=forms.TextInput(attrs={'placeholder': 'ideas, topics, interests, etc.',  'autofocus' : "autofocus", 'class' : 'input-xlarge '})
    )

class UserForm(forms.Form):
    password = forms.CharField(
    	label='',
    	widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'passcode', 'class' : 'input-small password-field ', 'autofocus' : "autofocus", 'maxlength' : '4'})
    )

