from django.db import models
from app.models import *

# Create your models here.
class Cartlist(models.Model):
    cart_id = models.CharField(max_length=250,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id 

class ItemsFree(models.Model):

    productF = models.ForeignKey(ProductFree,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cartlist,on_delete=models.CASCADE)
    quantF = models.IntegerField()
    Active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.productF)

    def total(self):
        return self.productF.price*self.quantF
   
