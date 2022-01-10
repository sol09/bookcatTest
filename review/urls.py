from django.urls import path
from . import views
from .models import User, Review

urlpatterns = [
    path('write/', views.write, name='write'),
    path('', views.index, name='list'),
    #path(str(reviewT.reviewId)+'/', views.review)
]