from rest_framework.generics import RetrieveDestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from base.models.inventory import Inventory
from base.models.category import Category
from .serializers import *
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters




class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class SalesRegisterAPIView(generics.GenericAPIView):
    serializer_class = SalesRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class CustomerRegisterAPIView(generics.GenericAPIView):
    serializer_class = CustomerRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })



class SupplierListAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = SupplierDetailsSerializer
    queryset = Supplier.objects.filter()
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category', 'in_stock']
    filter_backends = [filters.SearchFilter]
    search_fields = ['phone_numner', 'fullname']


class CategoryListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = CategoryDetailsSerializer
    queryset = Category.objects.filter()



class InventoryCreateAPIView(CreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = InventoryListSerializer
    queryset = Inventory.objects.filter()

    """ 
    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author) 
    """

    def perform_create(self, serializer):
        u = self.request.user
        user = User.objects.get(id=u)
        return serializer.save(user=user)



class InventoryListAPIView(ListAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = InventoryListSerializer
    queryset = Inventory.objects.filter()




class SupplierDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = SupplierDetailsSerializer
    queryset = Supplier.objects.filter()


class CategoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = CategoryDetailsSerializer
    queryset = Category.objects.filter()



class InventoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = InventoryListSerializer
    lookup_url_kwarg = 'pk'
    queryset = Inventory.objects.filter()




class OrderCreateAPIView(CreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        seller = User.object.get(id=user)
        return serializer.save(seller=seller)




class OrderListAPIView(ListAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = OrderListSerializer
    queryset = Order.objects.filter()


class SellerOrderListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    
    serializer_class = OrderSerializer
    model = serializer_class.Meta.model
    paginate_by = 100


    def get_queryset(self):
        return Order.objects.filter(seller=self.kwargs['user_id'])




class OrderItemCreateAPIView(CreateAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = OrderItemSerializer
    


class SellerOrderItemListAPIView(ListAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = OrderItemSerializer
    model = serializer_class.Meta.model
    paginate_by = 100


    def get_queryset(self):
        return Inventory.objects.filter(seller=self.kwargs['user_id'])

    '''
    def get_queryset(self):
        buyer = self.kwargs[self.requuest.user]
        queryset = self.model.objects.filter(user=buyer)
        return queryset.order_by('-created_at')
    '''


class SellerOrderItemRetreiveDeleteAPIView(RetrieveDestroyAPIView):
    """
    API view to retrieve list of posts or create new
    """
    serializer_class = OrderItemSerializer
    model = serializer_class.Meta.model
    paginate_by = 100


    def get_queryset(self):
        return Inventory.objects.filter(seller=self.kwargs['user_id'])




class OrderItemDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete post
    """
    serializer_class = OrderItemSerializer
    queryset = Inventory.objects.filter()



    




