from django.shortcuts import render
from .serializer import Newsserializer
from rest_framework import status
from rest_framework.response import Response
from .models import News
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class news_home_page(APIView):
    def get(self, request, format=None):
        news = News.objects.all()
        serializer = Newsserializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        current_user = request.user
        new_news = News(reporter=current_user)
        serializer = Newsserializer(new_news, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class news_detail_page(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, slug, format=None):
        single_news = News.objects.get(slug=slug)
        serialized = Newsserializer(single_news)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug, format=None):
        single_news = News.objects.get(slug=slug)
        current_user = request.user
        if current_user != single_news.reporter:
            return Response("You cannot edit someone's news")
        else:
            serializer = Newsserializer(single_news, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response({"message": "News update Successfully",
                            "data": serializer.data}, status=status.HTTP_202_ACCEPTED)
    
    
    def delete(self, request, slug, format=None):
        single_news = News.objects.get(slug=slug)
        current_user = request.user
        if current_user != single_news.reporter:
            return Response("Stop it!!!")
        else:
            single_news.delete()
            return Response("News has been deleted", status=status.HTTP_204_NO_CONTENT)


