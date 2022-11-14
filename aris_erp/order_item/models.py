from django.db import models
from aris_erp.Customer.models import Customer
from aris_erp.order.models import Order
from aris_erp.product.models import Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{}".format(self.id)

    def get_cost(self):
        return self.price * self.quantity
