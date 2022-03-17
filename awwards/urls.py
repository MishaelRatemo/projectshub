from django.urls import path
from . import views
urlpatterns = [
        
                path('', views.home, name='index' ),
                path('projects/<int:project_id>/',views.projects,name='projects'),
                path('profile/', views.profile, name='profile'),
                path('profile/<username>/settings', views.edit_profile, name='edit_profile'),
                path('upload_project/',views.post_project,name='post_project'),
                path('search/', views.search_project, name='search_results'),  
                path('logout', views.logout, name='logout'),

              ]