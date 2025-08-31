from django.db.models.aggregates import Count
from decimal import Decimal
import django.db.models
from rest_framework import serializers
from store.models import Cart, Collection, Product, Review


class CollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Collection
		fields = ['id', 'title', 'products_count']

	products_count = serializers.IntegerField(read_only=True)



class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax','collection']
		# fields ='__all__' to get all fields (bad practice)


	price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
	def calculate_tax(self, product: Product):
		return product.unit_price * Decimal(1.1)
	

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = ['id', 'date', 'name', 'description', 'product']
	
	def create(self, validated_data):
		product_id = self.context['product_id']
		return Review.objects.create(product_id=product_id, **validated_data)
	

class CartSerializer(serializers.ModelSerializer):
	id = serializers.UUIDField(read_only=True)
	class Meta:
		model = Cart
		fields = ['id', 'items'] 
		# comment
	






























	# {
	# 	"title": "good shoes",
	# 	"slug": "good-shoes",
	# 	"unit_price": 56.99,
	# 	"collection": 3,
	# 	"inventory": 12
	# }
	