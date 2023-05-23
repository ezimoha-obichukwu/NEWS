from django.shortcuts import render
from .serializer import Newsserializer
from rest_framework import status
from rest_framework.response import Response
from .models import News
from rest_framework.views import APIView

# Create your views here.
class news_home_page(APIView):
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = Newsserializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = Newsserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


