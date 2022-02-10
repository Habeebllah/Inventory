from django.db import models
from base.models.base import BaseEntity
from base.models.users import User


class Sales(BaseEntity):
    oursales = models.OneToOneField(User, related_name='sales', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, unique=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='sales/%Y/%m/%d', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.phone_number
   