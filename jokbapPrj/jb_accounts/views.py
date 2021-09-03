from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile


def signup(request):
    if request.method == "POST":
        if request.POST["password"]== request.POST["check_password"]:
            user=User.objects.create_user(username=request.POST["userID"],
                                          password=request.POST["password"])
            profile=Profile(user=user, name=request.POST["username"])
            profile.save()
            auth.login(request,user)
            return redirect('home')
        return render(request, 'signup.html')    
    else:
        
        return render(request, 'signup.html')


def login(request):
    if request.method=="POST" :
        userID= request.POST['userID']
        password= request.POST['password']
        user=auth.authenticate(request, username=userID, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, '아이디 또는 비밀번호가 일치하지 않습니다.')
            return render(request, 'login.html',{'error' : 'username or password is incorrect. '})

    else:
        return render(request, 'login.html')




