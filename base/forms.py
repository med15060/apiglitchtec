from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User=get_user_model()
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']



class ApplyForm(forms.ModelForm):
    introduction = forms.CharField(label = "introduction")
    zip= forms.CharField(label = "zip")
    rate= forms.CharField(label = "rate")
    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name','phone','email','rate','specializes','address',
        'country','state','zip','introduction' ,"profile_picture",
"resumate"]
    def save(self, request, user):
        user = super(ApplyForm, self).save(commit=False)
        user.descreption = self.cleaned_data['introduction']
        user.zip_code=self.cleaned_data['zip']
        user.save()
        profile = Profile.objects.get(user=user)
        return user


"""
class ApplyForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','phone','rate','specializes','address','conuntry','state','zip','introduction']
"""
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','account_status']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messageinfo
        fields = ['name','email','mess']


class QuForm(forms.ModelForm):
    class Meta:
        model = Quizz
        fields = ['name','email','color','date','bio','food','filee']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
