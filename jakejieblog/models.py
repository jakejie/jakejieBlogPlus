from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from DjangoUeditor.models import UEditorField


# 用户表 继承了auth模块
class UserProfile(AbstractUser):
    display_name = models.CharField(max_length=100, verbose_name="展示名称", default="")
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="male", max_length=8)
    address = models.CharField(max_length=100, default="", verbose_name="住址")
    mobile = models.CharField(max_length=11, default="", verbose_name="手机号码")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(verbose_name='文章类型', max_length=30)
    url = models.CharField(verbose_name="分配链接", max_length=30, default="")
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "文章类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(verbose_name='标签名', max_length=30)
    url = models.CharField(verbose_name="分配链接", max_length=30, default="")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        ordering = ['add_time']
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=200)  # 博客标题
    category = models.ForeignKey(Category, verbose_name=u'文章类型', on_delete=models.CASCADE)
    date_time = models.DateField(auto_now_add=True, verbose_name="博客日期")  # 博客日期
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)  # 博客发布具体时间
    # content = models.TextField(blank=True, null=True)  # 文章正文
    # content = models.TextField(blank=True, null=True, verbose_name="博客正文")  # 文章正文
    # content = UEditorField(verbose_name="博客正文", width=800, height=500, toolbars="full",
    #                        imagePath="article/ueditor/%Y/%m/", filePath="article/ueditor/%Y/%m/",
    #                        upload_settings={"imageMaxSize": 1204000}, default='')
    content = UEditorField(verbose_name="文章正文", width=800, height=500, toolbars="full",
                           imagePath="article/%%Y/%%m/", filePath="article/%%Y/%%m",
                           upload_settings={"imageMaxSize": 1204000}, default='')

    digest = models.TextField(blank=True, null=True, verbose_name="文章摘要")  # 文章摘要
    author = models.ForeignKey(UserProfile, verbose_name='作者', on_delete=models.CASCADE)
    view = models.BigIntegerField(default=0, verbose_name="阅读数")  # 阅读数
    comment = models.BigIntegerField(default=0, verbose_name="评论数")  # 评论数
    # picture = models.CharField(max_length=200, verbose_name="标题图片地址")  # 标题图片地址
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg",
                              verbose_name="标题图片", max_length=100)
    tag = models.ManyToManyField(Tag, verbose_name="标签")  # 标签

    # tag = models.ManyToOneRel(Tag, verbose_name="标签")  # 标签

    def __str__(self):
        return self.title

    def sourceUrl(self):
        source_url = settings.HOST + '/blog/detail/{id}'.format(id=self.pk)
        return source_url  # 给网易云跟帖使用

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])

    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])

    class Meta:  # 按时间降序
        ordering = ['-date_time']
        verbose_name = "文章列表"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    title = models.CharField(verbose_name="标题", max_length=100)
    source_id = models.CharField(verbose_name='文章id或source名称', max_length=25)
    create_time = models.DateTimeField(verbose_name='评论时间', auto_now=True)
    user_name = models.CharField(verbose_name='评论用户', max_length=25)
    url = models.CharField(verbose_name='链接', max_length=100)
    comment = models.CharField(verbose_name='评论内容', max_length=500)

    class Meta:
        ordering = ['create_time']
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name
