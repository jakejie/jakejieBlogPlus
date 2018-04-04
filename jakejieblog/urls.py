# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:DJBlog
FileName = PyCharm
Version:1.0
CreateDay:2018/4/4 9:11
"""
from django.urls import path
from .views import IndexView, ArticleList, ArticleDetail, ArticleCategoryView, \
    ArticleSearch, ArticleTag, AboutMe, Link, Message, GetComment, Archive

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('articles', ArticleList.as_view(), name="articles"),
    path('article/detail/<int:pk>', ArticleDetail.as_view(), name="detail"),
    path('search', ArticleSearch.as_view(), name="search"),
    path('article/tag/<str:name>', ArticleTag.as_view(), name="article_tag"),
    path('about/me', AboutMe.as_view(), name="about"),
    path('link', Link.as_view(), name="link"),
    path('message', Message.as_view(), name="message"),
    path('comment', GetComment.as_view(), name="comment"),
    path('archive', Archive.as_view(), name="archive"),
    # 按照文章类型获取列表
    path('article/category/<category_url>', ArticleCategoryView.as_view(), name="category")
]
if __name__ == "__main__":
    pass
