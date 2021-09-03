from django.shortcuts import render,redirect

def loading(request):
    return render(request,'Loading.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request,'Home.html')

def jpage(request):
    return render(request,'j_page.html' )

def bpage(request):
    return render(request,'b_page.html')

def bContent(request):
    return render(request, 'Content_Bap.html')

def jContent(request):
    return render(request, 'Content_Jok.html')