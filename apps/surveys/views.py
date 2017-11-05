from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "welcome to survey index"
    return HttpResponse(response)

def surveying(request):
    response = "resonding to the surveying request"
    return HttpResponse(response)
# Create your views here.
