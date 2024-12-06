from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('submit/', views.submit_review, name='submit_review'),
]
