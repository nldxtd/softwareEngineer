from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def hello(request):
    return JsonResponse({
        'code': 200,
        'data': 'Hello world!'
    })
