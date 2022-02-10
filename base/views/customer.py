from base.models.users import User
from django.shortcuts import render, redirect
from django.views.generic import ListView





class CustomerItemView(ListView):
    template_name = 'customer/customer_list.html'
    model = User
    context_object_name = 'customer'
    paginate_by = 15

    def get_queryset(self):
        queryset = super(CustomerItemView, self).get_queryset()
        queryset = queryset.filter(is_customer=True)
        return queryset


def CustomerOrderView(request):
    pass






