from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    '''
    function to return the homepage of the application
    '''
    pic = Image.objects.all()
    return render(request,'index.html',{'pic': pic})

def image(request,pic_id):
    '''
    function that returns pages to store individual images
    '''
    pic = Image.get_image(id=pic_id)
    return render(request,'image.html',{'item': pic})

def profile(request,iden):
    '''
    function that returns individual profiles
    '''
    person = Profile.get_profile(identity=iden)
    posts = Image.get_post(jina=iden)
    return render(request,'profile.html',{'human':person,'posts':posts})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.name = current_user
            profile.save()
        return redirect('home')

    else:
        form = EditProfileForm()

    return render(request,'new_profile.html',{"form":form})
