from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_sales = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
