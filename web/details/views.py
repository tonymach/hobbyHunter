from django.shortcuts import render
from django.http import HttpResponse
w = HttpResponse("Works!")

def index(request):
    return render(request,'details/index.html')
