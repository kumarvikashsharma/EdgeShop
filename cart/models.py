from django.db import models
from django.contrib.auth.models import User
from product.models import product

class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

def __str__(self):
    return f'{self.user},{self.product},{self.quantity}'

