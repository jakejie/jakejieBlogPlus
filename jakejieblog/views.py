import json
from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse
# 基于类的视图 继承类
from django.views.generic.base import View
# 引入需要的数据表
from .models import UserProfile
# 定义使用邮箱进行登陆 重载方法
from django.contrib.auth.backends import ModelBackend
# 发送激活、找回密码邮件
# 完成并集查询
from django.db.models import Q
# 导入表单操作

from django.views.decorators.csrf import csrf_exempt
# 导入定义的模型
from .models import Category, Tag, Article, Comment
# 对数据库找出来的内容进行分页
from django.core.paginator import Paginator
from DJBlog.settings import PAGE_SETTING


# 博客首页
class IndexView(View):
    def get(self, request):
        article_list = Article.objects.all().order_by('-date_time')[0:5]
        return render(request, 'jakejieblog/index.html',
                      {"article_list": article_list,
                       "source_id": "index"})

    def post(self, request):
        pass


# 博客文章列表
class ArticleList(View):
    def get(self, request):
        articles = Article.objects.all().order_by('add_time')
        paginator = Paginator(articles, PAGE_SETTING)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        count = len(articles)
        return render(request, 'jakejieblog/articles.html',
                      {"contacts": contacts,
                       "count": count, })

    def post(self, request):
        pass


class ArticleCategoryView(View):
    def get(self, request, category_url):
        articles = Article.objects.filter(category__url=category_url).all().order_by('add_time')
        count = len(articles)
        paginator = Paginator(articles, PAGE_SETTING)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, 'jakejieblog/articles.html',
                      {"contacts": contacts,
                       "count": count,
                       "category": Category.objects.filter(
                           url=category_url).first().name,
                       })


# 文章详情
class ArticleDetail(View):
    def get(self, request, pk):
        article = Article.objects.filter(id=pk).first()
        article.viewed()
        return render(request, 'jakejieblog/detail.html',
                      {"article": article,
                       "source_id": article.id})

    def post(self, request):
        pass


# 搜索
class ArticleSearch(View):
    def get(self, request):
        key = request.GET['key']
        articles = Article.objects.filter(title__contains=key).all().order_by('add_time')
        count = len(articles)
        paginator = Paginator(articles, 20)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)

        return render(request, 'jakejieblog/search.html',
                      {"contacts": contacts,
                       "count": count,
                       "key": key})

    def post(self, request):
        pass


# 标签
class ArticleTag(View):
    def get(self, request, name):
        articles = Article.objects.filter(tag__url=name).all()
        count = len(articles)
        paginator = Paginator(articles, PAGE_SETTING)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, 'jakejieblog/tag.html',
                      {"contacts": contacts,
                       "count": count,
                       "tag": Tag.objects.filter(url=name).first().tag_name})

    def post(self, request):
        pass


# 关于我
class AboutMe(View):
    def get(self, request):
        return render(request, 'jakejieblog/about.html')

    def post(self, request):
        pass


# 归档
class Archive(View):
    def get(self, request):
        article_list = Article.objects.order_by('-date_time')
        return render(request, 'jakejieblog/archive.html',
                      {"article_list": article_list})

    def post(self, request):
        pass


# 链接
class Link(View):
    def get(self, request):
        return render(request, 'jakejieblog/link.html')

    def post(self, request):
        pass


# 消息
class Message(View):
    def get(self, request):
        return render(request, 'jakejieblog/message_board.html', {"source_id": "message"})

    def post(self, request):
        pass


# 接收评论
class GetComment(View):
    @csrf_exempt
    def get(self, request):
        """
         接收畅言的评论回推， post方式回推
         :param request:
         :return:
         """
        arg = request.POST
        data = arg.get('data')
        data = json.loads(data)
        title = data.get('title')
        url = data.get('url')
        source_id = data.get('sourceid')
        if source_id not in ['message']:
            article = Article.objects.get(pk=source_id)
            article.commenced()
        comments = data.get('comments')[0]
        content = comments.get('content')
        user = comments.get('user').get('nickname')
        Comment(title=title, source_id=source_id, user_name=user, url=url, comment=content).save()
        return JsonResponse({"status": "ok"})

    def post(self, request):
        pass


# 重构 允许使用邮箱/用户名进行登陆
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
            # else:
            #     return None
        except Exception as e:
            return None
