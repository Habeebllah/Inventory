from django.forms import ModelForm
from django.forms import TextInput, NumberInput, EmailInput

from base.models.order import Order, OrderItem
from base.models.users import User
from django import forms


class OrderForm(ModelForm):
    buyer = forms.ModelChoiceField(queryset=User.objects.filter(is_customer=True))

    class Meta:
        model = Order
        fields = ('buyer',)

        """ widgets = {
            'full_name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter Full Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter email address'}),
            'phn_number': NumberInput(attrs={'class': 'form-control', 'id': 'phn_number'}),
            'address': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter address'})
        } """

