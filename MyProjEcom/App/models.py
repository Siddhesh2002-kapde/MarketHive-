from re import M
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    

class MainCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory,related_name = "subcategories", on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)


    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products/')


    def __str__(self):
        return self.name
    
    def is_in_stock(self):
        return self.stock>0
    
    def adjust_stock(self,quantity):
        self.stock = models.F('stock')-quantity
        self.save()


class Cart(models.Model):
    user = models.ForeignKey(UserProfle, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)
    added_at = models.DateTimeField(auto_now_add = True)


    def total_price(self):
        return self.product.price * self.quantity
    


class Order(models.Model):
    STATUS_CHOICES =(
        ('Processing', 'Processing'),
         ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),

    )
    
    user = models.ForeignKey(UserProfle, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default = 'Processing')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return f"Order {self.id} - {self.user.user.username}"
    
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def item_total(self):
        return self.product.price * self.quantity


