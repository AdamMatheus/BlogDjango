from distutils.command.upload import upload
from email.mime import image
from random import choices
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified= models.BooleanField(default=False)
    token= models.CharField(max_length=100)


class BlogModel(models.Model):
    title=models.CharField(max_length=1000)
    content=FroalaField()
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    user=models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now_add=True)
    upload_to=models.DateTimeField(auto_now=True)
    liked= models.ManyToManyField(User, default=None, blank=True ,related_name='liked')
   
    
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
        
    @property
    def num_likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES=(
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user=models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    post=models.ForeignKey(BlogModel, on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES, default='Like' ,max_length=10)
 


class Comment(models.Model):
    post=models.ForeignKey(BlogModel, related_name='comments', on_delete=models.CASCADE) 
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s -%s' % (self.post.title, self.name)
    