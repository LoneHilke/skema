from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Skema


# Create your views here.
def index(request):
    myskema = Skema.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'myskema': myskema
   }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({},request))

def addrecord(request):
  navn = request.POST['navn']
  gruppe = request.POST['gruppe']
  mandag = request.POST['mandag']
  tirsdag = request.POST['tirsdag']
  onsdag = request.POST['onsdag']
  torsdag = request.POST['torsdag']
  fredag = request.POST['fredag']
  pligter = request.POST['pligter']
  skema = Skema(navn=navn, gruppe=gruppe, mandag=mandag, tirsdag=tirsdag, onsdag=onsdag, torsdag=torsdag,fredag=fredag, pligter=pligter)
  skema.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  skema =Skema.objects.get(id=id)
  skema.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  myskema = Skema.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myskema': myskema,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  navn = request.POST['navn']
  gruppe = request.POST['gruppe']
  mandag = request.POST['mandag']
  tirsdag = request.POST['tirsdag']
  onsdag = request.POST['onsdag']
  torsdag = request.POST['torsdag']
  fredag = request.POST['fredag']
  pligter = request.POST['pligter']
  skema = Skema.objects.get(id=id)
  skema.navn = navn
  skema.gruppe = gruppe
  skema.mandag = mandag
  skema.tirsdag = tirsdag
  skema.onsdag = onsdag
  skema.torsdag = torsdag
  skema.fredag = fredag
  skema.pligter = pligter
  skema.save()
  return HttpResponseRedirect(reverse('index'))
  

