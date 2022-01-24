from django.urls import path, include
from . import views
from rest_framework import routers

from django.views.generic import TemplateView

from django.conf.urls import url

# DB api 보기
router = routers.DefaultRouter()
router.register('review', views.ReviewView, 'Review')
router.register('user', views.UserView, 'User')

urlpatterns = [
    path('', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('detail/<int:reviewId>/', views.detail, name='detail'),

    # DRF 사용하는 url
    path('api/', include(router.urls))
]