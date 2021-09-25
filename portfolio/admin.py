from django.contrib import admin
from .models import Project    #importing the class project from models.py

admin.site.register(Project)  #Registers the Project on the Site
