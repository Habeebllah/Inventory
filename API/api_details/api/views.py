from rest_framework import generics
from shop.models import Product
from .serializers import ProductSerializer


class ListProductsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer