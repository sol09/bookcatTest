from django.shortcuts import render
from .models import reviewT

def index(request):
    """리뷰 목록 출력"""
    review_list = reviewT.objects.order_by('-reviewId')
    context = {'rv_list': review_list}
    return render(request, 'write/review_list.html', context)