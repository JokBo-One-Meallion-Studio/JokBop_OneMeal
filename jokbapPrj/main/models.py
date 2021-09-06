from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Jok_Post( models.Model):
    title=models.TextField(max_length=100)
    pub_date= models.DateTimeField('date published') #최초 저장시에만 현재 날짜 적용
    text= models.TextField(max_length=2000) 
    image = models.ImageField(upload_to='photos/%m/%d', blank=True) # media/photos/월/날짜 폴더에 저장 
    author= models.ForeignKey(User, related_name='J_posts', on_delete =models.CASCADE)
    

    def __str__(self):
        return "text:" + self.text
    def summary(self):
        return self.text[:100]

class Jok_comment( models.Model ):
    author= models.ForeignKey(User, related_name='j_comments', on_delete=models.CASCADE)
    post=models.ForeignKey(Jok_Post, related_name='J_comments', on_delete= models.CASCADE)
    text= models.TextField(max_length=1000)
    pub_date=models.DateTimeField('date published')

class Bob_Post( models.Model):
    title=models.TextField(max_length=100)
    pub_date= models.DateTimeField('date published') #최초 저장시에만 현재 날짜 적용
    text= models.TextField(max_length=2000) 
    image = models.ImageField(upload_to='photos/%m/%d', blank=True) # media/photos/월/날짜 폴더에 저장 
    author= models.ForeignKey(User, related_name='B_comments', on_delete =models.CASCADE)
    
    def __str__(self):
            return "text:" + self.text
    def summary(self):
        return self.text[:100]

class Bob_comment( models.Model ):
    author= models.ForeignKey(User, related_name='b_comments', on_delete=models.CASCADE)
    post=models.ForeignKey(Bob_Post, related_name='B_comments', on_delete= models.CASCADE)
    text= models.TextField(max_length=1000)
    pub_date=models.DateTimeField('date published')

   

