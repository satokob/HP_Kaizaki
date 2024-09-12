from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News

def news_view(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 5)  # 1ページに5件表示

    page_number = request.GET.get('page')
    news_list = paginator.get_page(page_number)

    return render(request, 'news.html', {'news_list': news_list})