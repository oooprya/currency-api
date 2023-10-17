from django.contrib import admin
from django.urls import path, include
from api.models import ExchangerResource
from tastypie.api import Api


app_name = 'Home'

api = Api(api_name='v1')
exchanger_resource = ExchangerResource()
api.register(exchanger_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currency/', include('currency.urls')),
    path('', include('render.urls')),
    path('api/', include(api.urls)),
]
