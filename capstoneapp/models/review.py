from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .customer import Customer
from .business import Business


class Review(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    comment = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now=True)
    business = models.ForeignKey(
        Business, related_name="businesss", on_delete=models.CASCADE)

    class Meta:
        ordering = (F('created_at').asc(nulls_last=True),)
