from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE ,blank=True,null=True)
    name=models.CharField(max_length=200, blank =True)
    email=models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=200, blank =True)
    price=models.FloatField()
    digital=models.BooleanField(default=False)
    image=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name

    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    date_ordered=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
    @property
    def total_order(self):
        items=self.orderitem_set.all()
        total=sum([item.total for item in items])
        
        return total
    @property
    def total_items(self):
        items=self.orderitem_set.all()
        total=sum([item.quantity for item in items])
        return total
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)

    @property
    def total(self):
        total=self.product.price*self.quantity
        return total
    
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    city=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    date_added=models.DateField(auto_now_add=True)

    