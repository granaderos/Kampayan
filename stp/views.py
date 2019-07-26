from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers

from .models import CustomUser
from .models import Label
from .models import Ally

def index(request):
    return render(request, "stp/index.html")

def login(request):
    return render(request, "stp/LoginCustomer.html")

def sketch(request):
    return render(request, "stp/drag.html")

def smart_watch(request):
    return render(request, "stp/Smartwatch.html")

def set_time(request):
    return render(request, "stp/SetTime.html")

def home(request):
    return render(request, "stp/LandingPage.html")

def create_customer(request):
    return render(request, "stp/RegisterCustomer.html")

def offline(request): 
    return render(request, "stp/offline.html")

@csrf_exempt
def execute_login(request):
    email = request.POST["email"]
    password = request.POST["password"]

    try:
        user = CustomUser.objects.get(email=email, password=password)
        message = "Exists."
    except CustomUser.DoesNotExist:
        message = "Does not exist."
        user = {}
    # user = serializers.serialize('json', list(user))
    first_name = ""
    last_name = ""
    if(message == "Exists."):
        first_name = user.first_name
        last_name = user.last_name
    
    return JsonResponse({"message": message, "first_name": first_name, "last_name": last_name})


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

    allies = request.POST.getlist("allies")
    print("ALLIES=================")
    print(allies)

    for ally in allies:
        print("ally: --- ")
        print(ally)
        a = Ally.object.create(user=user_id, name=ally["name"], contact_number=ally["contact_number"])
        a.save()

    return JsonResponse({"message": "successful", "user": str(user_id)})

@csrf_exempt
def addLabel(request):
    user = request.POST["user_id"]
    latitude = request.POST.get("latitude", 0)
    longitude = request.POST.get("longitude", 0)
    location = request.POST["location"]
    label = request.POST["label"]

    entry = Label.objects.create(user=user, latitude=latitude, longitude=longitude, location=location, label=label)
    entry.save()