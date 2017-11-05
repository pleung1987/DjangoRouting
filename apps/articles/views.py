from django.shortcuts import render, redirect, HttpResponse

print "*"*20
print "got to articles.views"
print "*"*20
# Create your views here.
def index(request):
    return HttpResponse("Welcome to the articles page index")

def special_case_2003(request):
    return HttpResponse("special_case_2003 method")

def show(request, number):
    print number
    return HttpResponse("show method: " + number)

def show_word(request, word):
    return HttpResponse("show method:" + word)

def year_archive(request, year):
    return HttpResponse("showing year:" + year)

def month_archive(request, year, month):
    return HttpResponse("showing Year: " + year + " and month: " + month)
