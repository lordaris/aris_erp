import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Order
from .forms import OrderItemForm


def order_index_view(request):
    return render(request, "order_item/order_item_detail.html")


def order_list_view(request):
    return render(
        request,
        "order/order_list.html",
        {
            "orders": Order.objects.all(),
        },
    )


def order_add_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "customerListChanged": None,
                            "showMessage": f"{order.customer} added.",
                        }
                    )
                },
            )
    else:
        form = OrderForm()
    return render(
        request,
        "order/order_form.html",
        {
            "form": form,
        },
    )


def order_edit_view(request, pk):
    orders = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "customerListChanged": None,  # It's used to upload the page after submit the edition (or creation).
                            "showMessage": f"{orders.customer} updated.",
                        }
                    )
                },
            )
    else:
        form = OrderForm(instance=orders)

    return render(
        request,
        "order/order_form.html",
        {
            "form": form,
            "orders": orders,
        },
    )


@require_POST
def order_delete_view(request, pk):
    orders = get_object_or_404(Order, pk=pk)
    orders.delete()
    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": json.dumps(
                {
                    "CustomerListChanged": None,
                    "showMessage": f"{orders.customer} deleted.",
                }
            )
        },
    )
