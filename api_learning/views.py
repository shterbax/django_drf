from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api_learning.models import Article
from api_learning.serializers import ArticlesSerializer, ArticleSerializer


@api_view(["GET"])
def hello(request):
    return Response(data={"Message": "Hello world"}, status=status.HTTP_200_OK)


class ArticleAPI(APIView):

    def get(self, request):
        try:
            id = request.query_params["id"]

            if id is not None:
                article = Article.objects.get(id=id)
                serializer = ArticleSerializer(instance=article)
        except:
            articles = Article.objects.all().values()
            serializer = ArticlesSerializer(instance=articles, many=True)

        data = serializer.data

        return Response(data={"article": data}, status=status.HTTP_200_OK)
