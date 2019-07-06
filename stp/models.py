from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.

class CustomUser(models.Model):
    # user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    contact_number = models.CharField(max_length=50, null=True, blank=True, default="")
    password = models.CharField(max_length=50, null=False, blank=False)

    bank_name = models.CharFiled(max_length=50, null=False, blank=False)
    account_number = models.CharField(max_length=50, null=False, blank=False)