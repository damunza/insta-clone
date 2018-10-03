from django.shortcuts import render

# Create your views here.
def home(request):
    '''
    function to return the homepage of the application
    '''
    return render(request,'index.html')