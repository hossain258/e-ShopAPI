from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib import messages

# models import
from django.contrib.auth.models import User
from App_UserProfile.models import UserProfile

# Create your views here.

# def User_logout(request):
#     logout(request)
#     return redirect('home')
    
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            # extend  code here 

            
            
        # try:
        #     # if(username  != None or email != None or phone != None or password != None):
        #     #     messages.success(request, 'opps 😎! Please, Fillup your all information.That are very inportant information to create your account')
        #     #     return render(request, 'registration/sign_up.html')

            

            #Check email already exits or not
            exist_email = UserProfile.objects.filter(email=request.POST.email).first()
            if(exist_email):
                messages.success(request, 'opps 😛! Your email already Exits!.')
                return render(request, 'registration/sign_up.html')
            user = form.save()

        #     # Check phone number already exits or not
        #     exist_phone = UserProfile.objects.filter(phone=phone).first()
        #     if(exist_phone):
        #         messages.success(request, 'opps 😛! Your phone number already Exits!.')
        #         return render(request, 'registration/sign_up.html')
            
            login(request, user)
            messages.success(request,'Registarion submission successful')
            return redirect('login')
        # except Exception as e:
        #     messages.success(request, e)
        #     return render(request, 'registration/sign_up.html')

            
     
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form':form})

