from tastypie.resources import ModelResource
from currency.models import Exchanger, CartItem
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


data_curr = CartItem.objects.all()

class ExchangerResource(ModelResource):
    class Meta:
        queryset = Exchanger.objects.all()
        resource_name = 'exchangers'
        allowed_methods = ['get', 'post','delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.id = bundle.data['id']
        bundle.obj.address = bundle.data['address']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['currency'] =  {str(curr):{"buy": curr.buy, "sell": curr.sell} for curr in data_curr if bundle.obj.address == curr.cart.address}
        return bundle