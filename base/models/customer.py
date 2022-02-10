from django.db import models
from base.models.base import BaseEntity
from base.models.users import User


class Customer(BaseEntity):
    ourcustomer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, unique=True)
    nin_number = models.IntegerField(unique=True, null=True, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='customer/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    

    def __str__(self):
        return self.shop_name[:15]


    def get_customer_full_name(self):
        return self.customer.full_name_get()
   
