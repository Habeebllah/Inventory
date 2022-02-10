from django.db.models import fields
from rest_framework import serializers
from base.models.users import *
from base.models.customer import *
from base.models.sales import *
from base.models.category import *
from base.models.supplier import *
from base.models.inventory import *
from base.models.order import *
from django.contrib.auth import authenticate


User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class SalesRegisterSerializer(serializers.ModelSerializer):

    phone_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        phone_number = validated_data["phone_number"]
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_sales = True
        user.save()
        Sales.objects.create(oursales=user, phone_number=phone_number)
        return user




class CustomerRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        phone_number = validated_data["phone_number"]
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_customer = True
        user.save()
        Customer.objects.create(ourcustomer=user, phone_number=phone_number)
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class CustomerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('phone_number', 'address')


class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'category_image')


class SupplierDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('oursale', 'phone_number', 'address', 'profile_picture')


class InventoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        exclude = ('user', )
        #fields = ('category_name', 'supplier', )


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('id', )
        #fields = ('category_name', 'supplier', )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('buyer', 'seller')





class OrderListSerializer(serializers.ModelSerializer):

   

    class Meta:
        model = Order
        fields = ('buyer', 'seller', 'ref_code')


class OrderItemSerializer(serializers.ModelSerializer):

    #items_name = serializers.ReadOnlyField()
    #product = ProductListSerializer(many=False)
    #product = serializers.RelatedField(source='inventrory.id', read_only=True)



    #product = serializers.HyperlinkedRelatedField(view_name='orderitem-view', lookup_field='pk', many=False,
    #read_only=False, queryset=Inventory.objects.all())

    #subcategory_name = serializers.RelatedField(source='subcategory.id', read_only=True)
    #subcategory_set = SubCategoryOrderSerializer(many=True)
    #subcategory = serializers.StringRelatedField(source='subcategory.id', read_only=True)
    #items = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

       

  

class OrderItemDetailsSerializer(serializers.ModelSerializer):

    #subcategory_name = serializers.RelatedField(source='subcategory.id', read_only=True)
    #subcategory_set = SubCategoryOrderSerializer(many=True)
    #subcategory = serializers.StringRelatedField(source='subcategory.id', read_only=True)
    get_total_item_price = serializers.CharField(read_only=True)
    get_total_discount_item_price = serializers.CharField(read_only=True)
    get_amount_saved = serializers.CharField(read_only=True)
    get_final_price = serializers.CharField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'get_total_item_price',
                  'get_total_discount_item_price', 'get_amount_saved', 'get_final_price')

   

