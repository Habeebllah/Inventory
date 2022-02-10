from base.models.inventory import Inventory
from django.db import models
from base.models.base import BaseEntity
from base.models.inventory import Inventory


class Cart(BaseEntity):
    products = models.ManyToManyField(Inventory, null=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.total
