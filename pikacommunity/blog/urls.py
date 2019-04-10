from django.urls import path,include
from .views import BlogHomeView,BlogDetailView,BlogPulishView

urlpatterns = [
    path('',BlogHomeView.as_view(),name='blog_home'),
    path('detail/<blog_id>/',BlogDetailView.as_view(),name='blog_detail'),
    path('publish/',BlogPulishView.as_view(),name='blog_publish'),
]