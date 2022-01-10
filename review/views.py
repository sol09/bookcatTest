from django.shortcuts import render, redirect
from .models import Review, User

def index(request):
    """리뷰 목록 출력"""
    review_list = Review.objects.order_by('-reviewId')
    context = {'review_list': review_list}
    return render(request, 'review/list.html', context)

def review(request):
    """선택한 리뷰 출력"""
    rv = Review.objects.get(Review.reviewId)
    context = {'rv': rv}
    return render(request, 'review/detail.html', context)

def write(request):
    user = User.objects.get(userId='002')
    context = {'user':user}
    if request.method == 'POST':
        Review.objects.create(
            userId = user,
            bookId=request.POST['bid'],
            reviewId=request.POST['rid'],
            reviewTxt=request.POST['review']
        )
        return redirect('list')
    return render(request, 'review/write.html', context)