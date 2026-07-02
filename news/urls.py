from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('sports/',views.sports,name='sports'),
    path("politics/", views.politics, name="politics"),
    path("technology/", views.technology, name="technology"),
    path("business/", views.business, name="business"),
    path("entertainment/", views.entertainment, name="entertainment"),
    path("search/", views.search, name="search"),
    # path("category/<str:category_name>/",views.category_news,name='category_news'),
]
