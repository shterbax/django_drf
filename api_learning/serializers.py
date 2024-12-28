from rest_framework import serializers

from api_learning.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["title", "content", "author"]