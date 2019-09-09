from django import forms
from django.contrib.auth.models import User
from basicapp.model import note_model,user_model

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password') 
    
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = user_model.UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class CreateForm(forms.ModelForm):
    class Meta():
        model = note_model.Note
        fields = ('title','content')


        