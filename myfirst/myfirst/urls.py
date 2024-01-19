"""
URL configuration for myfirst project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myfirst import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('',views.homepage,name="home"),
    path('about-us/',views.aboutUs,name="about"),
    path('gallery/',views.gallery,name="gallery"),
    path('contact/',views.contact,name="contact"),
    path('course/<courseid>',views.coursedata),
    path('userforms',views.Userform),
    path('userform1/',views.Userform1),
    path('postuser',views.postform),
    path('postuser1',views.postform1),
    path('submitform/',views.submitform,name="submitform"),
    path('newsdetails/<newsid>',views.newsdetails),
]
