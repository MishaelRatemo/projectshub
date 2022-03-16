from django.urls import path
from . import views
urlpatterns = [
        
                path('', views.home, name='index' ),
                path('projects/<int:id>',views.projects,name='projects'),
                path('profile/<username>', views.profile, name='profile'),
                path('uploads/',views.post_project,name='post_site'),
                path('search/', views.search_project, name='search_results'),  

              ]