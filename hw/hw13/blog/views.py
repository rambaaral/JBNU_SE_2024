from django.shortcuts import render
from .models import Post, Category

def index(request):
    return render(
        request,
        'blog/index.html',
        {
            'title': 'main'
        }
    )

def blog_list(request):
    posts = Post.objects.all().order_by('-pk')
    return render(
        request,
        'blog/blog_list.html',
        {
            'title': 'blog',
            'subtitle': '블로그',
            'posts': posts
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'blog/single_post_page.html',
        {
            'title': 'blog_detail',
            'subtitle': '블로그_상세',
            'post': post
        }
    )

def about_me(request):
    return render(
        request,
        'blog/about_me.html',
        {
            'title': 'about us',
            'subtitle': '어바웃 어스'
        }
    )
"""
def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/blog_list.html',
        {
        'post_list': post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'category': category,
        }
    )
"""