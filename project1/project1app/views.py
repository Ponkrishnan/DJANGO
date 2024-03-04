from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'html1.html')
def index1(request):
    return render(request,'html2.html')
def index2(request):
    return render(request,'html3.html')
def index3(request):
    return render(request,'html4.html')