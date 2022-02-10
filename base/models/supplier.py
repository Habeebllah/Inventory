from django.db import models

from base.models.base import BaseEntity
from base.models.category import Category
from base.models.users import User


class Supplier(BaseEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=True)
    fullname = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    company = models.CharField(max_length=150, null=True, blank=True)
   
    def __str__(self):
        return self.fullname