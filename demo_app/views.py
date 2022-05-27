from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def index(request):
    json_payload = {
        "message": "Hello World!"
    }
    return JsonResponse(json_payload)