
from django.db import models



class SignUp(models.Model):
    Name = models.CharField(max_length=200,blank=True,null=True)
    Email= models.EmailField(max_length=200,blank=True,null=True)
    Password= models.CharField(max_length=200,blank=True,null=True)
    Address=models.CharField(max_length=500,blank=True,null=True)
    City=models.CharField(max_length=200,blank=True,null=True)
    State=models.CharField(max_length=200,blank=True,null=True)
    Zip =models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.Name

class Customer_Support (models.Model):
    Email= models.EmailField(max_length=200,blank=True,null=True)
    Comment = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.Email
    
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
 