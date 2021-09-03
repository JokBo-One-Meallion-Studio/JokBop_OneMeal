from django.shortcuts import get_object_or_404, render,redirect
from .models import Bob_Post
from .models import Jok_Post

def loading(request):
    return render(request,'Loading.html')

def home(request):
    return render(request,'Home.html')

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
    return render(request,'b_page.html')

def bContent(request):
    return render(request, 'Content_Bap.html')


