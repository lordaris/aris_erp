from .models import OrderItem
from django.forms import ModelForm


class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"
