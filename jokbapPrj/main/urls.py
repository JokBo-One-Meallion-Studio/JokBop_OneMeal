from django.urls import path    
from . import views

urlpatterns = [
    path('',views.loading,name="loading"), #로딩페이지
    path('home/',views.home,name="home"),
    path('home/myprofile',views.myProfile,name="myprofile"),
    path('home/myprofile/editprofile',views.editProfile,name="editprofile"),
    path('home/myprofile/editprofileImg',views.editProfileImg, name="edit_profileImg"),
    path('home/myprofile/eidtprofileInfo',views.editProfileInfo,name="editProfileInfo"),
    path('jpage/',views.jpage,name="j_page"),
    path('bpage/',views.bpage, name="b_page"),
    path('jpage_content/<int:j_id>',views.jContent,name="jContent"), #족글 자세히 보기
    path('bpage_content/<int:b_id>',views.bContent,name="bContent"), #밥메 자세히 보기
    # path('jpage/create_jokbo',views.createJokbo,name='new_jokbo'), #족보판매글 작성
    # path('jpage/create_bap',views.createBap,name='new_bap'),
    path('jpage/upload_jokbo',views.uploadJok,name='upload_jok'),
    path('jpage/upload_bap',views.uploadBap,name='upload_bap'),
    path('jpage_content/delete/<int:post_id>',views.j_delete,name='j_delete'),
    path('bpage_content/delete/<int:post_id>',views.b_delete,name='b_delete'),
    path('jpage/<int:j_id>/newComment',views.j_comment,name="j_newComment"),
    path('bpage/<int:b_id>/newComment',views.b_comment,name="b_newComment"),

   
    
    
]