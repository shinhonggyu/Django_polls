from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, worild. You're at the polls index.")
    
