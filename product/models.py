from ast import Delete
from itertools import product
from winreg import FlushKey
from xml.dom.minidom import CharacterData
from django.db import models

class productCategory(models.Model):
    name=models.CharField(max_length=150)
    status=models.BooleanField(default=True)

    def __str__(self):
        """" String representation of the product Category """
        return str(self.name)


class product(models.Model):
    product_category=models.ForeignKey(productCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    #description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    stock=models.IntegerField(default=1)
    cover_image=models.ImageField()
    status=models.BooleanField(default=True)

    def __str__(self):
        """String for representing the Model object."""
        return str(self.name)

class productImage(models.Model):
    """if product have more than one image """
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    image=models.ImageField()

    def __str__(self):
        """String for representing the Model object."""
        return str(self.product)   

class productFeatures(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    features=models.CharField(max_length=255)

# class productFeatures(models.Model):
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     feature=models.CharField(max_length=255)