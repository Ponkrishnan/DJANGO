from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index1(request):
    return HttpResponse("HEY ")
def p1(request):
    return HttpResponse("I")
def p2(request):
    return HttpResponse("Hate")
def p3(request):
    return HttpResponse("You")
def home(request):
    return HttpResponse("You")
def index2(request):
    return render(request,'index.html',)
def index(request):
    return render(request,'home.html',)