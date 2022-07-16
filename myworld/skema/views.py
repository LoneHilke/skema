from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Skema, Tlf


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
  
def tlf_index(request):
  mytlf = Tlf.objects.all().values()
  template = loader.get_template('tlf_index.html')
  context = {
    'mytlf': mytlf
  }
  return HttpResponse(template.render(context, request))
  
def tlf_add(request):
  template = loader.get_template('tlf_add.html')
  return HttpResponse(template.render({},request))

def tlf_addrecord(request):
  navn = request.POST['navn']
  tlf = request.POST['tlf']
  adresse = request.POST['adresse']
  arbejde = request.POST['arbejde']
  tlf = Tlf(navn=navn, tlf=tlf, adresse=adresse, arbejde=arbejde)
  tlf.save()
  return HttpResponseRedirect(reverse('tlf_index'))

def tlf_delete(request, id):
  tlf =Tlf.objects.get(id=id)
  tlf.delete()
  return HttpResponseRedirect(reverse('tlf_index'))

def tlf_update(request, id):
  mytlf = Tlf.objects.get(id=id)
  template = loader.get_template('tlf_update.html')
  context = {
    'mytlf': mytlf,
  }
  return HttpResponse(template.render(context, request))

def tlf_updaterecord(request, id):
  navn = request.POST['navn']
  tlf = request.POST['tlf']
  adresse = request.POST['adresse']
  arbejde = request.POST['arbejde']
  
  tlf = Tlf.objects.get(id=id)
  tlf.navn = navn
  tlf.tlf = tlf
  tlf.adresse = adresse
  tlf.arbejde = arbejde
  
  tlf.save()
  return HttpResponseRedirect(reverse('tlf_index'))
  