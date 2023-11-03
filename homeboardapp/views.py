from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.


def start_work(request):
    return render(request, 'homeboardapp/start_work.html')

def family_sns(request):
    return render(request, 'homeboardapp/family_sns.html')

def homeboard(request):
    return render(request, 'homeboardapp/homeboard.html')