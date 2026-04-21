from django.db.models import Sum, F
from django.utils.formats import number_format
from django.utils import timezone
from brands.models import Brand
from categories.models import Category
from products.models import Product
from outflows.models import Outflow


def get_product_metrics():
    products = Product.objects.all()
    total_cost_price = sum(product.cost_price * product.quantity for product in products)
    total_selling_price = sum(product.selling_price * product.quantity for product in products)
    total_quantity = sum(product.quantity for product in products)
    total_profit = total_selling_price - total_cost_price

    return dict(
        total_cost_price=number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        total_selling_price=number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity,
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
    )
