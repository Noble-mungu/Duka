from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) 
    email=models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='Duka/KwaDuka/profilepic')
    phone_number = models.CharField(max_length=20)
    
    @property
    def get_name(self):
        return self.user
        
    @property
    def get_id(self):
        return self.user.id
    
    
    
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to='Duka/KwaDuka/product_images')#Add the directory
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=1000)
    # category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    user=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)    
    
# class Category(models.Model):
#     name=models.CharField(max_length=50)
#     id=models.OneToOneField("Category", on_delete=models.CASCADE,primary_key=True)  
    
class Feedback(models.Model):
    name=models.CharField(max_length=50)
    feedback=models.CharField(max_length=500)
    date=models.DateField(auto_now=True,null=True) 
    
    def __str__(self):
        return self.name 
      
                           
                           
                           
                           
                           
                           
                           
    
    
    
    

    
