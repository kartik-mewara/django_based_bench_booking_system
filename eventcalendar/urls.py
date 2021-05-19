"""eventcalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import signup, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('calendar', include('calendarapp.urls')),
    path('bench1', include('bench1.urls')),
    path('bench2', include('bench2.urls')),
    path('bench3', include('bench3.urls')),
    path('bench4', include('bench4.urls')),
    path('bench5', include('bench5.urls')),
    path('bench6', include('bench6.urls')),
    path('bench7', include('bench7.urls')),   #edit here
    path('bench8', include('bench8.urls')),
    path('bench9', include('bench9.urls')),

]
