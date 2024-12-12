from django.forms import ModelForm
from .models import Blog 
from django import forms
class BlogForm(ModelForm):
    name = forms.CharField.widget=forms.TextInput(attrs={'class':'name', 'placeholder':'type ur idea...'})
    body = forms.Textarea.widget=forms.TextInput(attrs={'class':'area'})
    class Meta:
        model = Blog
        fields = ['name','body']
        labels = {
            'name':'',
            'body':''
            
        }

        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-group', 'row':30}),
        #     'body': forms.Textarea(attrs={'class':'form-group'}),
        # }
        
    
    