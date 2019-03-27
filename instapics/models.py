from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User=get_user_model()


class Profile(models.Model):
    profile_pic=models.ImageField(upload_to='images/',blank=True)
    bio=models.TextField()
    user=models.ForeignKey(User)
    
    def __str__(self):
        return self.bio
    @classmethod
    def my_profile(cls,user_id):
        profiles=Profile.objects.get(id=user_id)

        return profiles
    @classmethod
    def search_by_user(cls,query):
        result = cls.objects.filter(user__username__icontains=query)
        return result



        
class Image(models.Model):
    name=models.CharField(max_length=60)
    caption=models.CharField(max_length=100)
    gallery_image=models.ImageField(upload_to='images/')
    Profile=models.ForeignKey(Profile)
    url=models.CharField(max_length=100,blank=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    @classmethod
    def my_image(cls):
        images=Image.objects.all()

        return images
    def save_image(self):
        self.save()

    def delete_image(self):
        self.save()

    def update_caption(self):
        img= Image.objects.filter(id =1).update()


class Comment(models.Model):
    commented_by = models.ForeignKey(User)
    for_image = models.ForeignKey(Image,related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    body=models.TextField(default='SOME STRING')


class Likes(models.Model):
    likes=models.IntegerField()
    image=models.ForeignKey(Image,null=True)