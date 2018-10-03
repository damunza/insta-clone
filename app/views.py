from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    '''
    function to return the homepage of the application
    '''
    pic = Image.objects.all()
    return render(request,'index.html',{'pic': pic})
