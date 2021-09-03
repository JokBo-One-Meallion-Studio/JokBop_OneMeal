from django.urls import path    
from . import views

urlpatterns = [
    path('',views.loading,name="loading"), #로딩페이지
    path('home/',views.home,name="home"),
    path('jpage/',views.jpage,name="j_page"),
    path('bpage/',views.bpage, name="b_page"),
    path('jpage/content',views.jContent, name="Content_Jok"),
    path('bpage/content',views.bContent,name="Content_Bap"),
    path('jpage/create_jokbo',views.createJokbo,name='new'), #족보판매글 작성
]