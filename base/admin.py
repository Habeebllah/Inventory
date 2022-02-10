from django.contrib import admin

from base.models.category import Category
from base.models.tag import Tag
from base.models.inventory import Inventory
#from base.models.product import Product
from base.models.order import Order, OrderItem
from base.models.cart import Cart
from base.models.supplier import Supplier
from base.models.users import User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'update_at']
    list_display_links = ['name']
    # list_editable = ['name', 'parent']
    list_filter = ['name']
    list_per_page = 8


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(Supplier)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_name', 'current_stock', 'purchase_price', 'sales_price',
                    'promotional_price']
    list_display_links = ['name', 'category_name']
    list_editable = ['current_stock', 'purchase_price', 'sales_price', 'promotional_price']
    list_filter = ['name', 'current_stock']
    search_fields = ['name', 'purchase_price', 'sales_price', 'promotional_price']
    list_per_page = 8



admin.site.register(Inventory, InventoryAdmin)



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

admin.site.register(User)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'seller', 'get_grand_total']
    list_filter = ['completed', 'created_at', 'update_at']
    inlines = [OrderItemInline]
    #actions = [export_to_csv]
