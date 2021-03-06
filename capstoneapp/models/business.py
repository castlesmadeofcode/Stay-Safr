from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .customer import Customer
from .businessType import BusinessType


class Business(models.Model):

    name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/", null=True)
    address = models.CharField(max_length=75, null=True)
    website = models.CharField(max_length=75, null=True)
    created_at = models.DateTimeField(auto_now=True)
    business_type = models.ForeignKey(
        BusinessType, related_name="businesss", on_delete=models.DO_NOTHING)
    review_avg = 0

    # class Meta:
    # ordering = (F('created_at').asc(nulls_last=True),)

    def __str__(self):
        return self.name
