'''Product model define'''
from django.db import models
from .shops import Shop

# Create your models here.
class Product(models.Model):
    '''Product Model'''
    product_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='product_image', blank=True)
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True)
    purchase_price = models.PositiveIntegerField(blank=True)
    sale_price = models.PositiveIntegerField(blank=True)
    is_published = models.BooleanField(default=False)
