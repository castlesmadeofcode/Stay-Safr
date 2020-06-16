from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):

    user = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    image_path = models.CharField(max_length=250)
    is_owner = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Every time a `User` is created, a matching `Customer`
# object will be created and attached as a one-to-one
# property
@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, is_owner = False, address =  "", phone_number = 0, image_path = "")

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    instance.customer.save()


