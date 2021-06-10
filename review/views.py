from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Review

def index(request):
    review_list = Review.objects.all()
    context = {'review_list':review_list}
    return render(request, 'review/index.html', context)

def insertReview(request):
    return render(request, 'review/insertReview.html')

def completeReview(request):
    print(request.POST['content'])
    print(request.POST['author'])
    Review.objects.create(content=request.POST['content'], author=request.POST['author'])

    return index(request)
