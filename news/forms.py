from django import forms
from django.db import models
from django.forms import widgets
from django.forms.forms import Form
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','time_create',)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'tieude'}),
            'content' : forms.Textarea(attrs={'class' : 'content'})
        }   


class sendEmail(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'tieude'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'content', 'id':'noidung'}))
    cc = forms.BooleanField(required=False)