from django.urls import path
from store.views import (CartItemViewSet, CartViewSet, CollectionViewSet,
						  CustomerViewSet, ProductViewSet, ReviewViewSet, OrderViewSet)
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet)
router.register('carts', CartViewSet)
router.register('customers', CustomerViewSet)
router.register('orders', OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + products_router.urls + carts_router.urls