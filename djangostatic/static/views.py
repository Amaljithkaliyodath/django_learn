from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def index(request):
    return render (request,'index.html')


def awqw(request):
    return render(request,'awqw.html')