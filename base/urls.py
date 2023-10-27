from django.contrib import admin
from django.urls import path, include
from api.models import ExchangerResource, CartItemResource
from tastypie.api import Api


app_name = 'Home'
api = Api(api_name='v1')

cartitem_resource = CartItemResource()
exchanger_resource = ExchangerResource()
api.register(cartitem_resource)
api.register(exchanger_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls)),
]

