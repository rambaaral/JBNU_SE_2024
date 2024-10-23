from django.shortcuts import render
import json

# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html', 
        {'title': 'About_me', 'subtitle': '어바웃_미'}
    )

def blog_list(request):
    with open('./blog.json', 'r', encoding='utf-8') as f:
        blog = json.load(f)
    return render(
        request,
        'single_pages/blog_list.html', 
        {'title': 'Blog', 'subtitle': '블로그', 'posts': blog}
    )