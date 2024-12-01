from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.single_post_page, name='single_post_page'),
    path('', views.index, name='index'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('about_me', views.about_me, name='about_me')
]