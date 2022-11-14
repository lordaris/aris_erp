from django import forms
from .models import Customer
from django.forms import ModelForm



# Customer Forms 

class CustomerForm(ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control",
                "type": "text",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control",
                "type": "text",
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone Number",
                "class": "form-control",
                "type": "text",
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Email", "class": "form-control", "type": "email"}
        )
    )

    address_line_1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address Line 1",
                "class": "form-control",
                "type": "text",
            }
        )
    )
    address_line_2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Address Line 2",
                "class": "form-control",
                "type": "text",
            }
        )
    )
    postal_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Postal Code",
                "class": "form-control",
                "type": "number",
            }
        )
    )
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "City",
                "class": "form-control",
                "type": "text",
            }
        )
    )
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "State",
                "class": "form-control",
                "type": "text",
            }
        )
    )
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Country",
                "class": "form-control",
                "type": "text",
            }
        )
    )

    class Meta:
        model = Customer
        fields = "__all__"

