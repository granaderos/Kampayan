from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CustomUser
from .models import Label

@csrf_exempt
def addUser(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    contact_number = request.POST.get("contact_number", "")
    password = request.POST["password"]

    user = CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, contact_number=contact_number, password=password)
    user.save()

    user_id = CustomUser.objects.latest("id")

    return JsonResponse({"message": "successful", "user": user_id})

@csrf_exempt
def addLabel(request):
    user = request.POST["user_id"]
    latitude = request.POST.get("latitude", 0)
    longitude = request.POST.get("longitude", 0)
    location = request.POST["location"]
    label = request.POST["label"]

    entry = Label.objects.create(user=user, latitude=latitude, longitude=longitude, location=location, label=label)
    entry.save()