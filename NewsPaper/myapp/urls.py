from django.urls import path
from .views import PostList, PostDetail, SearchList
 
 
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search/', SearchList.as_view()),
]