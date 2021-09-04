from django.shortcuts import get_object_or_404, render,redirect
from .models import Bob_Post
from .models import Jok_Post

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

def bpage(request):
    posts=Bob_Post.objects.all()
    return render(request,'b_page.html',{"posts":posts})

def bContent(request, b_id):
    post= get_object_or_404(Bob_Post, pk=b_id)
    return render(request, 'Content_Bap.html',{"post":post})


