from django.urls import path

from . import views
from .views import ArticleAPI

urlpatterns = [
    path("", views.hello, name="index"),
    path("api/articles/", ArticleAPI.as_view(), name="articles"),
]