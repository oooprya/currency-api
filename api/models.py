from tastypie.resources import ModelResource
from currency.models import Exchanger, CartItem
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class ExchangerResource(ModelResource):
    class Meta:
        queryset = Exchanger.objects.all()
        resource_name = 'exchangers'
        allowed_methods = ['get', 'patch', 'post','delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.id = bundle.data['id']
        bundle.obj.address = bundle.data['address']
        return bundle

    def dehydrate(self, bundle):
        data_curr = CartItem.objects.all()
        bundle.data['currency'] =  {str(curr):{"buy": curr.buy, "sell": curr.sell, "sum": curr.sum} for curr in data_curr if bundle.obj.address == curr.cart.address}
        return bundle
