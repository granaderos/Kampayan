from django.db import models
from django.contrib.auth.models import User as AuthUser
import datetime


# Create your models here.

class CustomUser(models.Model):
    # user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False, default="")
    last_name = models.CharField(max_length=50, null=False, blank=False, default="")
    email = models.CharField(max_length=50, null=False, blank=False, default="")
    contact_number = models.CharField(max_length=50, null=True, blank=True, default="")
    password = models.CharField(max_length=50, null=False, blank=False, default="")

    bank_name = models.CharField(max_length=50, null=False, blank=False, default="")
    account_number = models.CharField(max_length=50, null=False, blank=False, default="")

class Merchant(models.Model):
    business_name = models.CharField(max_length=50, null=False, blank=False, default="")
    address = models.CharField(max_length=50, null=False, blank=False, default="")
    contact_person = models.CharField(max_length=50, null=False, blank=False, default="")
    contact_number = models.CharField(max_length=50, null=False, blank=False, default="")
    email = models.CharField(max_length=50, null=False, blank=False, default="")
    password = models.CharField(max_length=50, null=False, blank=False, default="")

class Transactions(models.Model):
    date = datetime.datetime.utcnow()
    user = models.ManyToManyField(CustomUser)
    merchant = models.ManyToManyField(Merchant)
    transaction_type = models.CharField(max_length=20, null=False, blank=False, default="save")
    status = models.IntegerField(default=0)
    amount = models.FloatField()
    current_savings = models.FloatField()
