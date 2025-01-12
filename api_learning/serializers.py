from rest_framework import serializers

from api_learning.models import Article


class ListArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["title", "content", "created_date"]

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["title", "content", "author"]