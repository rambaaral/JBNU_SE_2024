from django.urls import path
from . import views

app_name = "single_pages"

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'),
    path('about_me/', views.about_me, name='about_me'),
    path('', views.landing, name='landing'),
]