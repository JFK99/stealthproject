from django.contrib import admin #Import the admin  
from models import idea, UserProfile #Import our idea Model.  
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

  
admin.site.register(idea) #Register the model with the admin  
admin.site.register(UserProfile)