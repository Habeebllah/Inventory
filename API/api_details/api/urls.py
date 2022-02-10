from django.urls import path
from .views import ListProductsView



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('product/', ListProductsView.as_view(), name="all_product")
]