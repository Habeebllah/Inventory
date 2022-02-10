from base.models.order import OrderItem, Order
from django.shortcuts import render, redirect
from base.forms.order_form import OrderForm
from base.addcart import Cart
from django.views.generic import ListView
from base.models.users import User 
import random
import string


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


def bulling_information_view(request):
    customer = User.objects.filter(is_customer=True)
    print(request.user.id)
    #print(user)
    
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        #buyer = form.cleaned_data['buyer']
        #print(form.cleaned_data['buyer'])
        if form.is_valid():
            buyer = form.cleaned_data.get('buyer', None)
            order = form.save(commit=False)
            order.buyer = buyer
            order.seller = request.user
            order.save()

            for item in cart:
                OrderItem.objects.create(

                    
                    items=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return redirect('pos_view')
    else:
        form = OrderForm()
    return render(request, 'pos/billing_information.html', {'form': form, 'cart': cart, 'customer': customer})


class OrderItemView(ListView):
    template_name = 'pos/order_list.html'
    model = OrderItem
    context_object_name = 'order'
    paginate_by = 15

    def get_queryset(self):
        queryset = super(OrderItemView, self).get_queryset()
        queryset = queryset.filter(seller=self.request.user)
        return queryset





