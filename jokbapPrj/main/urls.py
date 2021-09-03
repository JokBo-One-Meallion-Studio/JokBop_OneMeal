from django.urls import path    
from . import views

urlpatterns = [
    path('',views.loading,name="loading"), #로딩페이지
    path('home/',views.home,name="home"),
    path('jpage/',views.jpage,name="j_page"),
    path('bpage/',views.bpage, name="b_page"),
    path('jdetail/<int:j_id>',views.jContent,name="jContent"), #족메뉴 더보기
    path('bpage/content',views.bContent,name="Content_Bap"),
    path('jpage/create_jokbo',views.createJokbo,name='new_jokbo'), #족보판매글 작성
    
]