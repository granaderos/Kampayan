from django.contrib import admin

from . models import CustomUser
from . models import Label
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Label)