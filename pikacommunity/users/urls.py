from django.urls import path
from .views import RegisterView,LoginView,ActiveUserView,LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('active/<active_code>',ActiveUserView.as_view(),name='active'),
    path('logout/',LogoutView.as_view(),name='logout')
]