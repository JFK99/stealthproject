import simplejson as json
from django.http import HttpResponse
from models import idea
from django.shortcuts import render_to_response  
from forms import ideaForm
from django.core.context_processors import csrf
from django.template import Context
from django.core import serializers
from helpers import dumps
from datetime import datetime

def home(request):
    return HttpResponse("Hello World")


def index(request): #Define our function, accept a request  
  
    #items = idea.objects.all() #ORM queries the database for all of the to-do entries.  
    
    c = Context({ 'idea_form': ideaForm()})
    
    return render_to_response('index.html', c) #Responds with passing the 


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
	items = idea.objects.all() #ORM queries the database for all of the to-do entries.  
	return HttpResponse("pull")	