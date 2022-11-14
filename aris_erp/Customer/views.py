from django.http import HttpResponse
from django.shortcuts import render
import json
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from .models import Customer
from .forms import CustomerForm


def customer_index_view(request):
    return render(request, "Customer/customer_detail.html")


def customer_list_view(request):
    return render(
        request,
        "Customer/customer_list.html",
        {
            "customers": Customer.objects.all(),
        },
    )


def customer_add_view(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "customerListChanged": None,
                            "showMessage": f"{customer.first_name} added.",
                        }
                    )
                },
            )
    else:
        form = CustomerForm()
    return render(
        request,
        "Customer/customer_form.html",
        {
            "form": form,
        },
    )


def customer_edit_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "customerListChanged": None,  # It's used to upload the page after submit the edition (or creation).
                            "showMessage": f"{customer.first_name} updated.",
                        }
                    )
                },
            )
    else:
        form = CustomerForm(instance=customer)

    return render(
        request,
        "Customer/customer_form.html",
        {
            "form": form,
            "customer": customer,
        },
    )


@require_POST
def customer_delete_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": json.dumps(
                {
                    "CustomerListChanged": None,
                    "showMessage": f"{customer.first_name} deleted.",
                }
            )
        },
    )
