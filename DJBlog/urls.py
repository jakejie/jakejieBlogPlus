"""DJBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# 图片正常显示
from django.views.static import serve
from DJBlog.settings import MEDIA_ROOT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
import xadmin
import DjangoUeditor

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # 富文本编辑器
    path('ueditor/', include('DjangoUeditor.urls')),
    # 图片显示配置
    path('media/<path:path>/', serve, {"document_root": MEDIA_ROOT}),

    path('blog/', include('jakejieblog.urls')),
]
# 设置静态文件路径
urlpatterns += staticfiles_urlpatterns()