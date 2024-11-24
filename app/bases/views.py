from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def primera_vista(request):
    return HttpResponse("Hola Mundo")