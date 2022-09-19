import imp
import re
from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import get_user_model


from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

# models import
from django.contrib.auth.models import User
from App_UserProfile.models import UserProfile

from .tokens import account_activation_token

# Create your views here.

# def User_logout(request):
#     logout(request)
#     return redirect('home')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation, now you can login')
    else:
        messages.success(request, 'Activation link is invalid!')
        
    return redirect('login')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account'
    message = render_to_string('template_active_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user} please to got your email {to_email} inbox and click on received activation link to congirm and complete the registration, Note: Check your span folder also')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check your type email')



    
def sign_up(request):
    if request.method == 'POST':
        reqEmail = request.POST['email']
        reqPhone = request.POST['phone']
        reqAddressline1 = request.POST['addressline1']
        reqAddressline2 = request.POST['addressline2']
        reqCity = request.POST['city']
        reqOtp = 123

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
                user = form.save(commit=False)
                user.is_active=False
                user.save()
            
                profile=UserProfile.objects.create(
                    username=user, 
                    email=reqEmail, 
                    phone=reqPhone, 
                    address=reqAddressline1,                
                    # addressline1=reqAddressline1,
                    # addressline2=reqAddressline2,
                    city=reqCity,
                    otp=reqOtp 
                )
                profile.save()
                # extend  code here 
                activateEmail(request, user, form.cleaned_data.get('email'))
                # login(request, user)
                # messages.success(request,'Registarion submission successful')
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

