from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News

def news_view(request):
    news_list = News.objects.all().order_by('published_date')
    paginator = Paginator(news_list, 5)  # 1ページに5件表示

    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)

    return render(request, 'news/news.html', {'news_list': news_list})

def blog_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', {'news_item': news_item})