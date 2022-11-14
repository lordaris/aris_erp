from django.urls import path

from . import views
from aris_erp.Customer.views import (
    customer_index_view,
    customer_add_view,
    customer_edit_view,
    customer_list_view,
    customer_delete_view,
)

app_name = "Customer"
urlpatterns = [
    path("", views.customer_index_view, name="customer_index"),
    path("add/", views.customer_add_view, name="add_customer"),
    path("<int:pk>/edit", views.customer_edit_view, name="edit_customer"),
    path("list/", views.customer_list_view, name="customer_list"),
    path("<int:pk>/remove", views.customer_delete_view, name="remove_customer"),
]
