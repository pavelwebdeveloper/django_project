from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#from django.template import loader

def home(request):
    #return HttpResponse("Hello world from my_photo_app coded in Python!")
    #template = loader.get_template('home.html')
    #return HttpResponse(template.render())
    return HttpResponse("Hello world from my_photo_app coded in Python!")


    #return render(request, "home.html", {})