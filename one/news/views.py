from django.shortcuts import render
from .models import News
# Create your views here.
def news_list(request):
    news_all = News.objects.all()
    context = {}
    context['list'] = news_all
    return render(request, 'list.html', context)

def news_content(request, news_id):
    news_ids = News.objects.get(id=news_id)
    context = {}
    context['content'] = news_ids
    return render(request,'detail.html', context)