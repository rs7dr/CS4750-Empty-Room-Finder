from django.http import HttpResponse
from django.shortcuts import render
#from .models import Post

def index(request):
    return HttpResponse("Hello, world. You're at the Empty Room Finder Homepage.")


#return http response or return a template.




