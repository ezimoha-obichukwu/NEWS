from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home_page.as_view(), name="home"),
    path('news/<slug:slug>/', views.news_detail_page.as_view(), name="details"),
]