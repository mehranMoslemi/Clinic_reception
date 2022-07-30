from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate , login as lg, logout as lgo
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username = username , password = password)
        if user is not None:
            lg(request, user)
            return redirect('index')
        else:
            messages.error(request , 'username or password is incorrect!')
            render(request,'accounts/login.html')
    return render(request,'accounts/login.html')

def logout(request):
    lgo(request)
    return render(request,'accounts/login.html')

