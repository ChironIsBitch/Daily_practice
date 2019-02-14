from django.urls import path
from .views import news_list, news_content
urlpatterns = [
    path('', news_list, name='list'),
    path('<int:news_id>', news_content, name='content')

]