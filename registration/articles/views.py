from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import IsEmailVerified
from articles.serializers import ArticleSerializer, ArticleDetailSerializer, ArticleCheckDetailsSerializer
from articles.models import Article


class UserArticleView(APIView):
    permission_classes = (IsAuthenticated, IsEmailVerified)

    def post(self, request):
        serializer = ArticleCheckDetailsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title, text = serializer.data.values()
        article = Article.objects.create(title=title, text=text, author=request.user)
        return Response(status=status.HTTP_201_CREATED,
                        data=ArticleDetailSerializer(article).data)

    def get(self, request):
        articles = Article.objects.all()
        serialized_articles = ArticleSerializer(articles, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized_articles.data)

class UserArticleDetailView(APIView):
    permission_classes = (IsAuthenticated, IsEmailVerified)

    def get(self, request, title):
        article = get_object_or_404(klass=Article, title=title)
        serializer = ArticleDetailSerializer(article)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
