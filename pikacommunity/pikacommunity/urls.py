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
from .settings import MEDIA_URL,MEDIA_ROOT
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from users.views import RegisterView
from tech.views import SuggestView,SearchView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),
    path('test/',TemplateView.as_view(template_name='test.html'),name='test'),
    path('suggest/',SuggestView.as_view(),name='suggest'),
    path('search',SearchView.as_view(),name='search')
]
