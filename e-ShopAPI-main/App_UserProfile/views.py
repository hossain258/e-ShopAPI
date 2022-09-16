import re
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
        reqEmail = request.POST['email']
        reqPhone = request.POST['phone']
        reqAddressline1 = request.POST['addressline1']
        reqAddressline2 = request.POST['addressline2']
        reqCity = request.POST['city']
        # reqOtp = request.POST['otp']

        if(User.objects.filter(email=reqEmail).exists()):
            messages.warning(request, 'opps 😛! Your email already Exits!.')
            # return render(request, 'registration/sign_up.html')
            return redirect (reverse_lazy("App_UserProfile:sign_up"))
        elif(UserProfile.objects.filter(phone=reqPhone).exists()):
            messages.success(request, 'opps 😛! Your phone number already Exits!.')
            return render(request, 'registration/sign_up.html')
        else:
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
            
                profile=UserProfile.objects.create(
                    username=user, 
                    email=reqEmail, 
                    phone=reqPhone, 
                    address=reqAddressline1,                
                    # addressline1=reqAddressline1,
                    # addressline2=reqAddressline2,
                    city=reqCity,
                    # otp=reqOtp 
                )
                profile.save()
            # extend  code here 

            
            
            # try:
            #     if(username  != None or email != None or phone != None or password != None):
            #         messages.success(request, 'opps 😎! Please, Fillup your all information.That are very inportant information to create your account')
            #         return render(request, 'registration/sign_up.html')

                # Check phone number already exits or not
                # exist_phone = UserProfile.objects.filter(phone=reqPhone).first()
                # if(exist_phone):
                #     messages.success(request, 'opps 😛! Your phone number already Exits!.')
                #     return render(request, 'registration/sign_up.html')
            
                login(request, user)
                messages.success(request,'Registarion submission successful')
                return redirect('login')



        # except Exception as e:
        #     messages.success(request, e)
        #     return render(request, 'registration/sign_up.html')

            
     
    else:
        form = RegisterForm()
        diction ={
            'form':form,
            }
    return render(request, 'registration/sign_up.html', context=diction)

