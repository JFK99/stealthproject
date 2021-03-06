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
from django.contrib.auth import authenticate, login


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
    newIdea = idea(created=now.strftime("%Y-%m-%d %H:%M:%S"), description=entry['idea_pushed'], viewed=False)
    newIdea.save()
    counter =  "#" + str(idea.objects.count()) + " PUSHED!" 

    response = {
            "success": True,
            "code": 0,
            "count":  counter
          }
    return HttpResponse(dumps(response), mimetype="application/json")    
    
	    
@csrf_exempt
def login(request):
    username=request.POST['login']
    password = request.POST['pin']
    user = authenticate(username=username, password=password)
    if user is not None:
    	if user.is_active:
    		response = {
        		"success": True,
     	   		"code": 0,
    		}
    else:
    	response = {
        	"success": True,
        	"code": 1,
    	}
	
    return HttpResponse(dumps(response), mimetype="application/json")    
@csrf_exempt
def pull(request):
	try:
		item = idea.objects.filter(viewed=False).order_by('?')[0]
		item.viewed = True
		item.save()
		response = {
			"success": True,
			"code": 0,
			"idea": item.description
		}
	except IndexError:
		response = {
			"success": True,
			"code": 0,
			"idea": "Oops, I'm out of idea, please refill me"
		}

	
	return HttpResponse(dumps(response), mimetype="application/json")    

@csrf_exempt
def stats(request):
    workflow_list = []
    columns = [{"id": "",
               "label": "State",
               "pattern": "",
               "type": "string"},
              {"id": "",
               "label": "Count",
               "pattern": "",
               "type": "string"},]
    
    rows = []
    viewed = {"c": [{"v": "Viewed", "f": "Viewed"},
                 {"v":  idea.objects.filter(viewed=True).count(), "f":  idea.objects.filter(viewed=True).count()}]
        }
    not_viewed = { "c": [{"v": "Not Viewed", "f": "Not Viewed"},
                     {"v":  idea.objects.filter(viewed=False).count(), "f":  idea.objects.filter(viewed=False).count()}]
        }

    rows.append(viewed)
    rows.append(not_viewed)
    
    workflow_list.append({'title': "Statistics",
                          'data': {"cols": columns, "rows": rows}})
    return HttpResponse(dumps(workflow_list), mimetype="application/json")


@csrf_exempt
def count(request):
    response = {
        "success" : True,
        "code"    : 0,
        "total" : idea.objects.count(),
        "viewed":  idea.objects.filter(viewed=True).count(),
        "not viewed":  idea.objects.filter(viewed=False).count()
    }
    return HttpResponse(dumps(response), mimetype="application/json")

def vault(request):
    group = models.Group.objects.get(name='PBNJ')
    users = UserProfile.objects.filter(user__in=group.user_set.all())
    
    c = Context({ 'user_form': UserForm(), 'users': users})
    return render_to_response("vault.html", c)
