"""pikacommunity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import xadmin
from django.conf import settings
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('users/',include('users.urls')),
    path('captcha/',include('captcha.urls')),
    path('test/',TemplateView.as_view(template_name='test.html'),name='test'),
    path('tech/',include('tech.urls')),
    path('blog/',include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)