from django.db import models
from .customer import Customer
from .business import Business


class RecommendedBusiness(models.Model):

    recommended_customer = models.ForeignKey(
        Customer, related_name='recommended_user', on_delete=models.CASCADE)
    recommending_customer = models.ForeignKey(
        Customer, related_name='logged_in_user', on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
