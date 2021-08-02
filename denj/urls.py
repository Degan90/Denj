from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('denjs/', views.DenjList.as_view(), name='denj_list'),
    path('denjs/<int:pk>',
         views.DenjDetail.as_view(), name='denj_detail'),
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
]