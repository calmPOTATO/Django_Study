from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insertReview/', views.insertReview, name='insertReview'),
    path('insertReview/complete/', views.completeReview, name='completeReview'),
]