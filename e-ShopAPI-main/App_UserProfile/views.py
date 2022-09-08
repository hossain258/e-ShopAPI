from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

# def User_logout(request):
#     logout(request)
#     return redirect('home')
    
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # extend your code here 


            login(request, user)

            # message here 
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form':form})

