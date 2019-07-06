from django.db import models
import datetime


# Create your models here.

class CustomUser(models.Model):
    # user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False, default="")
    last_name = models.CharField(max_length=50, null=False, blank=False, default="")
    email = models.CharField(max_length=50, null=False, blank=False, default="")
    contact_number = models.CharField(max_length=50, null=True, blank=True, default="")
    password = models.CharField(max_length=50, null=False, blank=False, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name

class Label(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=244, null=False, blank=False, default="")
    label = models.IntegerField()

    def __str__(self):
        return self.location + " - " + str(self.label)
 