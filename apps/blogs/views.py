from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response= "this is the blog index"
    return HttpResponse(response)

def new(request):
    response = "a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("this is blog: " + number)

def edit(request, number):
    return HttpResponse("You are edditing blog: " + number)

def destroy(request, number):
    return HttpResponse("You are deleting blog: " + number)
