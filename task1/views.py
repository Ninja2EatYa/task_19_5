from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from task1.models import Post

# Create your views here.


def all_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    context = {
        'title': 'Посты',
        'page': 'Всяческие посты',
        'all_posts': Post.objects.all(),
        'page_posts': page_posts
    }
    return render(request, 'base.html', context)


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'page_posts': page_posts})
