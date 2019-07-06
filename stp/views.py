from django.shortcuts import render
from django.http import JsonResponse

from .models import CustomUser

# Create your views here.
def users(request):
    users = CustomUser.objects.all().values()
    users = list(users)

    return JsonResponse({"users": users})