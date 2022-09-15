from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is my new page')

def home(request):
    return render(request, 'about.html')

def reverse(request):
    return render(request,'revers.html')