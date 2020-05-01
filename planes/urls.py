from django.urls import path, include
from planes import views
from django.contrib.auth import urls

urlpatterns = [
    path('', views.index),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')

]