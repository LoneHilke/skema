from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Skema


# Create your views here.
def index(request):
    myskema = Skema.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'myskema': myskema
   }
    return HttpResponse(template.render(context, request))
  
  #template = loader.get_template('my_first.html')
  #return HttpResponse(template.render())


