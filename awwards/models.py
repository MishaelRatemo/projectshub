from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile/', default='profile.png')
    user_bio = models.TextField(max_length=500, default="My Bio", blank=True)
    user_name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=16,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        super().save()
        
    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def filter_profile_by_id(cls,id): 
        profile = Profile.objects.filter(user = id).first()
        return profile

    
class ProjectPosts(models.Model): 
    profile = models.ForeignKey(User,null=True,on_delete=models.CASCADE) 
    title = models.CharField(max_length=20,blank=True)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    landing_page = models.ImageField(upload_to='proj_images/')
    description = HTMLField(max_length=200,blank=True)
    link = models.URLField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    
    class  Meta:
        ordering=['post_date']
        
        
    @classmethod
    def search_by_project_title(cls,search_title):
        projects = cls.objects.filter(title__icontains=search_title)
        print(projects)
        return projects 
    
    @classmethod
    def get_user_projects(cls,profile):
       projects = ProjectPosts.objects.filter(profile__pk=profile)
       print(projects)
       return projects
    
    
    def __str__(self):
        return self.title
    

class Ratings(models.Model):
    design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)]) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.IntegerField(default=0) 