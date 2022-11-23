from django.shortcuts import render

# Create your views here.
def login(request):
    return render (request,'login.html')
def namepage(request):
    return render (request,'namepage.html')