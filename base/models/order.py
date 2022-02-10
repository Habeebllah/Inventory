from django.db import models

from base.models.base import BaseEntity
from base.models.inventory import Inventory
from base.models.users import User

from base.models.coupon import Coupon


import random
import string


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


# order by user
class Order(BaseEntity):

    seller = models.ForeignKey(User, related_name="seller", on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, related_name="buyer", on_delete=models.CASCADE)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    ref_code = models.CharField(max_length=20, default=create_ref_code, blank=True, null=True)
    

    def __str__(self):
        return f"{self.buyer.first_name} - {self.ref_code}"


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_grand_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        #3if self.coupon:
        #    total -= self.coupon.amount
        return total  
    
    #full_name = models.CharField(max_length=60, blank=True, null=True)
    #phn_number = models.CharField(max_length=14, blank=True, null=True)
    #email = models.EmailField(blank=True, null=True)
    #address = models.CharField(max_length=150, blank=True, null=True)



""" # order Item list
class OrderItem(BaseEntity):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #orderItem = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    products = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
 """



class OrderItem(models.Model):
   
    items = models.ForeignKey(Order, related_name='items',  on_delete=models.CASCADE)
    #payment = models.ForeignKey(
    #    'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    #coupon = models.ForeignKey(
    #    'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
  
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    @property
    def items_name(self):
        return self.items.id

    @property
    def product_name(self):
        return self.product.name

    def __str__(self):
        return str(self.id)

    
   


    def get_total_item_price(self):
        return self.quantity * self.product.sales_price

    def get_total_discount_item_price(self):
        if self.product.promo:
            return self.quantity * self.product.promotional_price

    def get_amount_saved(self):
        if self.product.promo:
            return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.promo:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


  
