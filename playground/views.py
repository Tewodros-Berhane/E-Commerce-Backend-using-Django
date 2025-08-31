from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db import transaction, connection
from django.db.models import Q, Value, F, Func, Count, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg
from django.db.models.functions import Concat
from django.http import HttpResponse

from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem

# @transaction.atomic()
def say_hello(request):

	# 

	# with transaction.atomic():
	# 	order = Order()
	# 	order.customer_id = 1
	# 	order.save()

	# 	item = OrderItem()
	# 	item.order = order
	# 	item.product_id = 1 
	# 	item.quantity = 5
	# 	item.unit_price = 30
	# 	item.save()


	# raw sql query
	# Product.objects.raw('SELECT * FROM store_product')

	cursor = connection.cursor()
	cursor.execute('')
	cursor.close()

	with connection.cursor() as cursor:
		cursor.execute()
		cursor.callproc()

	# , {'results': query_set}
	return render(request, 'index.html')
