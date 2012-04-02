from django.http import HttpResponse
from models import idea, UserProfile
from django.shortcuts import render_to_response  
from forms import ideaForm, UserForm
from django.core.context_processors import csrf
from django.template import Context
from django.core import serializers
from helpers import dumps
from datetime import datetime
from django.contrib.auth import models
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return HttpResponse("")


def index(request): #Define our function, accept a request  
  
    #items = idea.objects.all() #ORM queries the database for all of the to-do entries.  
    
    c = Context({ 'idea_form': ideaForm()})
    return render_to_response('index.html', c) #Responds with passing the 

@csrf_exempt
def push(request):
    entry =  request.POST
    now = datetime.now()
    newIdea = idea(created=now.strftime("%Y-%m-%d %H:%M:%S"), description=entry['idea_pushed'], viewed='N')
    newIdea.save()
    response = {
            "success": True,
            "code": 0,
          }
    return HttpResponse(dumps(response), mimetype="application/json")    
    
	    

def login(request):
	return HttpResponse("login")	

def pull(request):
	items = idea.objects.all() #Query to get idea
	return HttpResponse("pull")

def vault(request):
    group = models.Group.objects.get(name='PBNJ')
    users = UserProfile.objects.filter(user__in=group.user_set.all())
    
    c = Context({ 'user_form': UserForm(), 'users': users})
    return render_to_response("vault.html", c)