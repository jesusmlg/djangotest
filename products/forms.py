from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

  title       = forms.CharField(label='', widget = forms.TextInput(attrs ={
                                            'placeholder' : "Write your title here"
                                          }))
  description = forms.CharField(
                      required = False, 
                      widget = forms.Textarea(attrs = {
                        'class' : "new-class-name two",
                        'rows': 20,
                        'cols': 120
                      })
                      )
  price       = forms.DecimalField(initial = 199.28)

  class Meta:
    model = Product
    fields = [
        'title', 'description', 'price'
    ]
  
  def clean_title(self,*args, **kargs):
    title = self.cleaned_data.get('title')
    if "JMLG" in title:
      return title
    else:
      raise forms.ValidationError("This is not a valid titleeeee!!!")


class RawProductForm(forms.Form):
  title       = forms.CharField(label='', widget = forms.TextInput(attrs ={
                                            'placeholder' : "Write your title here"
                                          }))
  description = forms.CharField(
                      required = False, 
                      widget = forms.Textarea(attrs = {
                        'class' : "new-class-name two",
                        'rows': 20,
                        'cols': 120
                      })
                      )
  price       = forms.DecimalField(initial = 199.28)

