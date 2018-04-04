# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:JakeBlog
FileName = PyCharm
Version:1.0
CreateDay:2018/3/23 16:32
"""

from jakejieblog.models import Category, Article, Tag, Comment


def sidebar(request):
    category_list = Category.objects.all().order_by('created_time')
    # 所有类型

    article_rank = Article.objects.all().order_by('-view')[0:6]
    # 文章排行

    tag_list = Tag.objects.all().order_by('add_time')
    # 标签

    comment = Comment.objects.all().order_by('-create_time')[0:6]
    # 评论

    return {
        'category_list': category_list,
        'article_rank': article_rank,
        'tag_list': tag_list,
        'comment_list': comment

    }


if __name__ == "__main__":
    pass
