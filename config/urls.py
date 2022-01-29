"""config URL Configuration

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

#from . import views

from review import views
from rest_framework import routers

from django.views.generic import TemplateView   # TemplateView 상속

'''
# DB 보기
router = routers.DefaultRouter()
router.register('review', views.ReviewView, 'Review')
router.register('user', views.UserView, 'User')
'''

urlpatterns = [
    #path('', views.ReactAppView.as_view),    # 이건 config/views
    #path('', TemplateView.as_view(template_name='index.html')),    # 이건 review/views
    # path('', views.index),    # 이건 review/views
    #path('write/', views.write, name='write'),    # review/views/write

    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('user/', include('user.urls')),
    #path('api/', include(router.urls))
]
