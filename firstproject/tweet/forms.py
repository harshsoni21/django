from django import forms
from .models import Tweet ,TweetInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta: 
        model = Tweet
        fields = ["text","photo" ,'category']
        widgets = {
            'text': forms.Textarea(attrs={'class' : 'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs = {'class':'form-select'}),
        }
        
class TweetInfo(forms.ModelForm):
    class Meta : 
        model = TweetInfo
        fields = ["tweetTags" , "tweetInfo",]    
        widgets = {
            'tweetTags' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'tweetInfo' : forms.TextInput(attrs = {'class':'form-control'}), 
        }    


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta :
        model = User
        fields = ('username','email','password1','password2')