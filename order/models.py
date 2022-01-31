from operator import mod
from django.db import models
from django.contrib.auth.models import User
from product.models import product

class order(models.Model):
    order_status_choice=(('pending','pending'),
    ('in progress','in progress'),
    ('Cancelled','Cancelled'),
    ('Delivered','Delivered')
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    order_status=models.CharField(max_length=255, choices=order_status_choice, default='pending')
    address=models.TextField()
    date_time=models.DateTimeField()
    payment_status=models.BooleanField(default=False)

def __str__(self):
    return str(self.id)

class orderDetail(models.Model):
    order=models.ForeignKey(order, on_delete=models.CASCADE)
    product=models.ForeignKey(product, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    quantity=models.IntegerField(default=1)

def __str__(self):
    return f'{self.order.id}-{self.product}'
