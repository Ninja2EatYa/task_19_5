from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    post_list = Post.objects.all()

    items_per_page = request.GET.get('items_per_page', 5)
    paginator = Paginator(post_list, items_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'task5/post_list.html', {'page_obj': page_obj})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Получаем пост по его первичному ключу
    return render(request, 'task5/post_detail.html', {'post': post})