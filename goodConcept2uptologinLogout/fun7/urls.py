"""fun7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from fun7app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('admin/', admin.site.urls),
    url(r'^mtv_studentrecords/',views.mtv,name='mtv_list'),
    # path(r'^homepage/',views.home,name='homepage'),
    url(r'^homepage/',views.home,name='homepage'),
    url(r'^register',views.register,name='registration'),
    url(r'^special/',views.special,name='special'),
    url('user_login/',views.login_for_user2 ,name='user_login'),
    url('user_logout/',views.user_logout,name='user_logout'),

# you can use  PATH AND URL BOTH
]
