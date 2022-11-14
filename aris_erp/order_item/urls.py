from django.urls import path
from . import views

app_name = "order_item"

urlpatterns = [
    path("", views.order_item_index_view, name="index_order_item"),
    path("add/", views.order_item_add_view, name="add_order_item"),
    path("<int:pk>/edit", views.order_edit_view, name="edit_order_item"),
    path("list/", views.order_list_view, name="list_order_item"),
    path("<int:pk>/remove", views.order_delete_view, name="remove_order_item"),
]
