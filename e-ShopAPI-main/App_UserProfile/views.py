from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.

def User_logout(request):
    logout(request)
    return redirect('home')
    