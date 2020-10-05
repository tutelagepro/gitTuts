from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError

# Create your models here.


def tv(t):
        if len(t)<15:
            raise ValidationError("Title length too short")

class Books(models.Model):
    
    title=models.CharField(validators=[tv],max_length=50)# this validator will be applicable
    #on custom form as well as admin panel
    #Comment 1
    #comment 2
    descr=models.CharField(max_length=150)
    author=models.CharField(max_length=50)
    price=models.FloatField()
    publisher=models.TextField(max_length=50)


    
class BooksForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=['title','descr','author','price','publisher']
        # if validator is applied here then it will be applicable on custom form only.




    