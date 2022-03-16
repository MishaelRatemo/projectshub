from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import ProjectPosts,Profile,Ratings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm,VotesForm,ProjectUploadForm

# Create your views here.
def home(request):
    all_projects = ProjectPosts.objects.all()
    context={
        'projects': all_projects,
    }
    return render(request, 'index.html', context)


@login_required(login_url='/accounts/login/')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('home')
    else:
        form =ProjectUploadForm()
    context={"form":form,}    
    return render(request,'uploads.html',context)


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

def user_profile(request, username):
    user_profile = get_object_or_404(User, username=username)
    if request.user == user_profile:
        return redirect('profile', username=request.user.username)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'userprofile.html', context)


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('profile', user.username)
    else:
        profile_form = EditProfileForm(instance=request.user.profile)
    context = {
        'prof_form': profile_form
    }
    return render(request, 'edit.html', context)


def search_project(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = ProjectPosts.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'
        context = {
            'results': results,
            'message': message
        }
        return render(request, 'searchresult.html', context)
    else:
        message = "Sorry Entered nothing in the search bar, Please try again"
    return render(request, 'searchresult.html', {'message': message})

def projects(request,project_id):
    try:
        projects = ProjectPosts.objects.get(id=project_id)
        all_votes = Ratings.objects.filter(project=project_id) 
        print(all)
    except Exception as ex:
        raise Http404() 
    
    # count user votes 
    count = 0
    for vote in all_votes:
        count+=vote.usability
        count+=vote.design
        count+=vote.content
    
    if count > 0:
        average = round(count/3,1)
    else:
        average = 0
        
    if request.method == 'POST':
        form = VotesForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project_id
            rate.save()
        return redirect('projects',project_id)
        
    else:
         form = VotesForm()
         
    votes = Ratings.objects.filter(project=project_id)
    #initialize empty ratings
    usability = []
    design = []
    content = [] 
    
    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content) 
        
    if len(usability) > 0 or len(design)>0 or len(content)>0:
        avg_usability = round(sum(usability)/len(usability),1) 
        avg_design = round(sum(design)/len(design),1)
        avg_content = round(sum(content)/len(content),1) 
            
        average_rating = round((avg_content+avg_design+avg_usability)/3,1) 
    
    else:
        avg_content=0.0
        avg_design=0.0
        avg_usability=0.0
        average_rating = 0.0
        
    # Restrict user to vote/ rate once
    
    arr1 = []
    for user_v in votes:
        arr1.append(user_v.user_id) 
                
    auth = arr1
       
    context = {
        'projects':projects,'form':form,'usability':avg_usability,'design':avg_design,
        'content':avg_content,'average_rating':average_rating, 'auth':auth,
        'all':all_votes, 'average':average,        
    }    
    return render(request,'single_post.html',context) 

