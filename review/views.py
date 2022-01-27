from django.shortcuts import render, redirect
#from .models import Review, User   # serializers를 통해 DB를 받았기 때문에 models import 불필요

from .serializers import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
import json

#class ReviewView(viewsets.ModelViewSet):
class ReviewView(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request):
        review_serializer = ReviewSerializer(data=request.data)
        if review_serializer.is_valid():
            review_serializer.save()
            return Response(review_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('reviewId') is None:
            review_qr_serializer = ReviewSerializer(Review.objects.all(), many=True)
            return Response(review_qr_serializer.data, status=status.HTTP_200_OK)
        else:
            reviewId = kwargs.get('reviewId')
            review_serializer = ReviewSerializer(Review.objects.get(id=reviewId))
            return Response(review_serializer.data, status=status.HTTP_200_OK)

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    return render(request, 'index.html')

def list(request):
    """리뷰 목록 출력"""
    review_list = Review.objects.order_by('-reviewId')
    context = {'review_list': review_list}
    return render(request, 'review/list.html', context)
    #reviews = ReviewView.queryset
    #review_list = reviews.__dict__
    #return JsonResponse(review_list, safe=False)

def write(request):
    """글쓰기"""
    user = User.objects.get(userId=1)
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