from os import name
from django.db import models
from base.models.users import User
from tenant_schemas.models import TenantMixin

""" class UserSubdomain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subdomain = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return f"User: {self.user} -- Subdomain: {self.subdomain}"

    def save(self, *args, **kwargs):
        self.subdomain = self.user.get_username()
        super().save(*args, **kwargs)
  """

class Users(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True