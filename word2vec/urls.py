from django.contrib import admin
from django.urls import path, include

from word2vec import views

urlpatterns = [
    path('query/', views.query),
    path('review/', views.review)
]
