from django.shortcuts import render, redirect
from .serializers import *
from rest_framework import viewsets
#from .models import Review, User   # serializers를 통해 DB를 받았기 때문에 models import 불필요

class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

def index(request):
    return render(request, 'index.html')

def list(request):
    """리뷰 목록 출력"""
    review_list = Review.objects.order_by('-reviewId')
    context = {'review_list': review_list}
    return render(request, 'review/list.html', context)

def write(request):
    """글쓰기"""
    user = User.objects.get(userId=2)
    context = {'user':user}
    if request.method == 'POST':
        Review.objects.create(
            userId = user,
            #bookId = request.POST['bid'],
            #reviewId = request.POST['rid'],
            bookId = '00000001',
            reviewId = 10,
            reviewTxt = request.POST['rtext']
        )
        return redirect('list')
    return render(request, 'review/write.html', context)

def detail(request, reviewId):
    """선택한 리뷰 출력"""
    review = Review.objects.get(reviewId=reviewId)
    user = User.objects.get(userId=review.userId)
    context = {'review': review, 'user': user}
    return render(request, 'review/detail.html', context)