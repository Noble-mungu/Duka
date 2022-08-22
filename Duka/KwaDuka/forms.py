from dataclasses import fields
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from  . import models 


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['first_name','last_name','username','password','address','mobile','profile_pic']
        widgets = {
        'password': forms.PasswordInput()
        }
class LoginUserForm(forms.modelForm):
    class Meta:
        model=models.Customer
        fields=['email','password']
        Widget = {
        'password':forms.PasswordInput()
        }
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))