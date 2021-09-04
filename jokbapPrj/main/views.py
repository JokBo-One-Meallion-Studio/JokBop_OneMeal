from django.shortcuts import get_object_or_404, render,redirect
from .models import Bob_Post
from .models import Jok_Post
from django.utils import timezone
from django.contrib.auth.models import User


def loading(request):
    return render(request,'Loading.html')

#차후 베스트글이 띄워지도록 함수를 수정해야함
def home(request):
    jok_posts= Jok_Post.objects.all()
    bob_posts=Bob_Post.objects.all()
    return render(request,'Home.html',{"j_posts":jok_posts, "b_posts":bob_posts})

def jpage(request):
    posts=Jok_Post.objects.all()
    return render(request,'j_page.html',{"posts":posts})

#'족' 상세페이지
def jContent(request, j_id):
    post= get_object_or_404(Jok_Post, pk=j_id)
    return render(request, 'Content_Jok.html',{"post":post})

#'족'작성페이지
def createJokbo(request):
    return render(request,'newJokbo.html')

#'밥'작성페이지
def createBap(request):
    return render(request,'newBap.html')

def uploadJok(request):
    new_Jok = Jok_Post()
    new_Jok.title = request.POST['title']
    new_Jok.pub_date = timezone.now()
    new_Jok.image = request.FILES['image']
    new_Jok.text = request.POST['text']
    new_Jok.author = request.user
    new_Jok.save()
    return redirect('j_page')

def uploadBap(request):
    new_Bob = Bob_Post()
    new_Bob.title = request.POST['title']
    new_Bob.pub_date = timezone.now()
    new_Bob.image = request.FILES['image']
    new_Bob.text = request.POST['text']
    new_Bob.author = request.user
    new_Bob.save()
    return redirect('b_page')

def bpage(request):
    posts=Bob_Post.objects.all()
    return render(request,'b_page.html',{"posts":posts})

def bContent(request, b_id):
    post= get_object_or_404(Bob_Post, pk=b_id)
    return render(request, 'Content_Bap.html',{"post":post})

    
def profile(request,author_id):
    author= get_object_or_404(User, pk=author_id)
    return render(request, 'profile.html',{'author':author}) 


def myProfile(request):
    user= request.user
    return render(request,'profile.html')