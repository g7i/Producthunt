from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])

                return render(request, 'accounts/signup.html',{'error':'User already exists.'})

            except User.DoesNotExist:
                User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'accounts/signup.html',{'error':'Password didn\'t match.'})
    
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            # if 'next' in request.POST:
            #     return redirect(request.POST.get('next'))
            # else:
            #     return redirect('home')
            return redirect(request.POST.get('next','home'))
        else:
            return render(request,'accounts/login.html',{'error':'Username or Password is incorrect..'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')