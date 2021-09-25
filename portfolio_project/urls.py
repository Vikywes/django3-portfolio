"""portfolio_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # This makes the url link active on the project site when click
from django.conf import settings   # This makes the settings.py available to //Media upload issue
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('base/', views.base, name = 'base'),

    path('blog/', include('blog.urls')),  #Refering users to blog project url - that we manually created
    #This is How to create another Django Urls in Django App //blog is just like empty path in blog app

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
#Add the above settings to make the images appear on the browser 
