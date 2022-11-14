from .models import Order
from aris_erp.Customer.models import Customer
from django.forms import ModelForm


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
