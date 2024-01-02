from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from .views import CustomLoginView

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('accounts/profile/', views.profiles , name='profiles'),
    path('logout/', auth_views.LogoutView.as_view() , name='logout'),
    ]