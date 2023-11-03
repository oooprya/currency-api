from tastypie.resources import ModelResource
from currency.models import Exchanger, CartItem
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication



class CartItemResource(ModelResource):
    class Meta:
        queryset = CartItem.objects.all()
        resource_name = 'cartitem'
        allowed_methods = ['get', 'put', 'post', 'patch','delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.cart_id = bundle.data['cart_id']
        bundle.obj.item_id = bundle.data['item_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['cart_id'] = bundle.obj.cart
        bundle.data['item_id'] = bundle.obj.item
        return bundle


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
