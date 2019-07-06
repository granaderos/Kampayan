from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CustomUser
from .models import Merchant

# Create your views here.
def users(request):
    users = CustomUser.objects.all().values()
    users = list(users)

    return JsonResponse({"users": users})

@csrf_exempt
def addUser(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    contact_number = request.POST.get("contact_number", "")
    password = request.POST["password"]
    bank_name = request.POST["bank_name"]
    account_number = request.POST["account_numer"]

    user = CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, contact_number=contact_number, password=password, bank_name=bank_name)
    user.save()

    user_id = CustomUser.objects.latest("id")

    return JsonResponse({"message": "successful", "customer_id": user_id})

@csrf_exempt
def addMerchant(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]
    contact_number = request.POST.get("contact_number", "")
    password = request.POST["password"]
    bank_name = request.POST["bank_name"]
    account_number = request.POST["account_numer"]

    user = CustomUser.objects.create(first_name=first_name, last_name=last_name, email=email, contact_number=contact_number, password=password, bank_name=bank_name)
    user.save()

    user_id = CustomUser.objects.latest("id")

    return JsonResponse({"message": "successful", "customer_id": user_id})

@csrf_exempt
def add_transaction(request):
    