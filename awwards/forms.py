from django import forms
from .models import Profile,ProjectPosts,Ratings


class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = ProjectPosts
        exclude =['post_date','profile','design','usability','content']
        
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image','user_bio','Location','phone') 
        
class VotesForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ('user','project')
        

