from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user= models.OneToOneField(User,related_name="profile", on_delete=models.CASCADE )
    profileImg = models.ImageField(upload_to='profileImg',blank=True)
    name= models.CharField(max_length=20, blank=True)
    intro=models.TextField(blank=True)