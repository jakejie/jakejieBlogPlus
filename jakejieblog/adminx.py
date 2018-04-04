# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:DJBlog
FileName = PyCharm
Version:1.0
CreateDay:2018/4/4 9:12
"""
from .models import Category, Tag, Article, Comment
import xadmin


class CategoryAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['name', 'url', 'created_time', 'last_mod_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['name', 'url', 'created_time', 'last_mod_time']
    # 配置筛选字段
    list_filter = ['name', 'url', 'created_time', 'last_mod_time']


class TagAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['tag_name', 'url', 'add_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['tag_name', 'url']
    # 配置筛选字段
    list_filter = ['tag_name', 'url', 'add_time']


class ArticleAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['title', 'category', 'add_time', 'author',
                    'view', 'comment', 'tag']
    # 配置搜索字段,不做时间搜索
    search_fields = ['title', 'category', 'author',
                     'view', 'comment', 'tag']
    # 配置筛选字段
    list_filter = ['title', 'category', 'add_time', 'author',
                   'view', 'comment', 'tag']
    # !!!!!!!!!重要!!!!!!!忘记了这步，找了很久！！
    # 参考https://blog.csdn.net/geerniya/article/details/79114711
    style_fields = {"content": "ueditor"}


class CommentAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['title', 'source_id', 'create_time', 'user_name',
                    'url', 'comment']
    # 配置搜索字段,不做时间搜索
    search_fields = ['title', 'source_id', 'create_time', 'user_name',
                     'url', 'comment']
    # 配置筛选字段
    list_filter = ['title', 'source_id', 'create_time', 'user_name',
                   'url', 'comment']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)

from xadmin import views


# 创建X admin的全局管理器并与view绑定。
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# xadmin全局配置
class GlobalSettings(object):
    site_title = "JakeJie博客后台管理系统"
    site_footer = "JakeJie博客管理系统"

    # 让管理后台左侧收起来
    # menu_style = "accordion"

    # def get_site_menu(self):
    #     return (
    #         {'title': '课程管理', 'menus': (
    #             {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
    #             {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
    #             {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
    #             {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
    #             {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
    #         )},
    #         {'title': '机构管理', 'menus': (
    #             {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
    #             {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
    #             {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
    #         )},
    #         {'title': '用户管理', 'menus': (
    #             {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
    #             {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
    #             {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
    #             {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
    #             {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
    #         )},
    #
    #         {'title': '系统管理', 'menus': (
    #             {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
    #             {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
    #             {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
    #             {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
    #             {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
    #         )},
    #     )


# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

if __name__ == "__main__":
    pass
