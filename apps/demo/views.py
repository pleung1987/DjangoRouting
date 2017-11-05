from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response= "We are at Demo's index"
    return HttpResponse(response)

def test(request):
    response= "We are at Demo's test"
    return HttpResponse(response)
