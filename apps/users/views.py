from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response= "welcome to the User Response"
    return HttpResponse(response)

def usering(request):
    response = "you are now going to the usering route"
    return HttpResponse(response)
