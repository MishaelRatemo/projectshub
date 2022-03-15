from django.contrib import admin
from .models import ProjectPosts,Profile,Ratings

# Register your models here.
admin.site.register(ProjectPosts)
admin.site.register(Profile)
admin.site.register(Ratings)

