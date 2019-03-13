from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
  title = forms.CharField(widget = forms.TextInput(
    attrs = {'placeholder': 'Write your title'}
  ))
  
  content = forms.CharField(widget = forms.Textarea(
    attrs = {'placeholder' : 'This is the place to write your text content'}
  ))

  active = forms.BooleanField(initial = True)

