from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home_page.as_view(), name="home"),
]