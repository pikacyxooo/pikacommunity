from django.urls import path,include
from django.views.generic.base import TemplateView
from .views import SuggestView,SearchView

urlpatterns = [
    path('suggest/', SuggestView.as_view(), name='suggest'),
    path('search', SearchView.as_view(), name='search'),
]