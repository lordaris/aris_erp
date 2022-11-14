from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=60, null=True)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, default="Mexico")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

