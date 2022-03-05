from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class categ(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prdt_by_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class ProductFree(models.Model):

    name=models.CharField(max_length=150,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    img=models.ImageField(upload_to='picture')
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(categ,on_delete=models.CASCADE)
    paid_or_free = models.TextField()


    def get_url(self):
        return reverse('details', args=[self.category.id, self.slug])      
    def __str__(self):
        return '{}'.format(self.name)