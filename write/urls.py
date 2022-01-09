from django.urls import path
from . import views
from .models import userT, reviewT

urlpatterns = [
    path('', views.index),
    #path(str(reviewT.reviewId)+'/', views.review)
]