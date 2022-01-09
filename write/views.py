from django.shortcuts import render
from .models import reviewT

def index(request):
    """리뷰 목록 출력"""
    review_list = reviewT.objects.order_by('-reviewId')
    context = {'review_list': review_list}
    return render(request, 'write/review_list.html', context)

def review(request):
    """선택한 리뷰 출력"""
    rv = reviewT.objects.get(reviewT.reviewId)
    context = {'rv': rv}
    return render(request, 'write/review.html', context)