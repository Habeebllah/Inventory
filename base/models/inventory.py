from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey

from base.models.base import BaseEntity
from base.models.category import Category
from base.models.tag import Tag
from base.models.supplier import *
from base.models.users import User



class Inventory(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productCategory')
    supplier = models.ForeignKey(Supplier, related_name='inventorysupplier', on_delete=models.CASCADE)
    short_description = models.CharField(max_length=250)
    full_description = models.TextField()
    current_stock = models.IntegerField(default=0)
    purchase_price = models.IntegerField(default=0)
    sales_price = models.IntegerField(default=0)
    promotional_price = models.IntegerField(default=0)
    promo = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='inventory_tag')
    picture = models.ImageField(upload_to='inventory/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_full_details(self):
        return f'{self.name}  --  {self.supplier.fullname}'
