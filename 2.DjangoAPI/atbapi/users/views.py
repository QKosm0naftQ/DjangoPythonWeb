from django.shortcuts import render

from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def get_all_users(request):
    users = User.objects.all().values("id", "username", "email")
    return JsonResponse(list(users), safe=False)

