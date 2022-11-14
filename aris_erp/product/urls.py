from django.urls import path
from . import views
from aris_erp.order.views import (
    order_index_view,
    order_add_view,
    order_edit_view,
    order_list_view,
    order_delete_view,
)

app_name = "order"

urlpatterns = [
    path("", views.order_index_view, name="order_index"),
    path("add/", views.order_add_view, name="add_order"),
    path("<int:pk>/edit", views.order_edit_view, name="edit_order"),
    path("list/", views.order_list_view, name="order_list"),
    path("<int:pk>/remove", views.order_delete_view, name="remove_order"),
]
