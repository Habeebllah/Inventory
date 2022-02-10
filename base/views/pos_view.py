from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from base.models.product import Product
from base.addcart import Cart
from base.models.inventory import Inventory
import json
from django.http import JsonResponse

from django.http import HttpResponse

def search_product(request):

    search_product = request.GET.get('product', '')
    
    products = Inventory.objects.all().values('name')

    mysearch = []

    if products:

        #result_products = Inventory.objects.filter(name__icontains=search_product)

        for product in products:
        
            mysearch.append(product)

            
    #dump = json.dumps(mysearch)
    #return HttpResponse(dump, content_type='application/json')
    return JsonResponse({"mysearch": mysearch}, status=200)




def POSView(request):


    if 'term' in request.GET:
        qs = Inventory.objects.filter(name__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.get_full_details())
            
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)

    product = Inventory.objects.filter()
        
    cart = Cart(request)
           

    for item in cart:
           
        item['update_quantity_form'] = {'quantity': item['quantity'], 'update': True}

    context = {
            
        'product': product,
        'cart': cart
    }

    
    template_name = 'pos/pos.html'
    return render(request, template_name, context)


# Add to cart views
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Inventory, id=id)
    print(product)
    cart.add(inventory=product, quantity=1, update_quantity=1)
    return redirect('pos_view')


# Remove Shopping Cart views
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Inventory, id=id)
    cart.remove(product)
    return redirect('pos_view')


# update Shopping Cart views
@require_POST
def cart_updated(request, id):
    number = None
    cart = Cart(request)
    if request.method == 'POST':
        number = int(request.POST.get('number'))
    product = get_object_or_404(Inventory, id=id)
    cart.add(inventory=product, quantity=number, update_quantity=True)
    return redirect('pos_view')
