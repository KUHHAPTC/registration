from rest_framework import serializers

from articles.models import Article
from users.serializers import UserDetailSerializer


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer()

    class Meta:
        model = Article
        fields = ('author', 'title', 'text', 'date', )


class ArticleCheckDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'text', )


class ArticleSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer()

    class Meta:
        model = Article
        fields = ('author', 'title', 'date', )
