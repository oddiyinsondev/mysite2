from django.urls import path
from .views import PostList, Postdetail, Apiviews


urlpatterns = [
    path('',  PostList.as_view()),
    path('<int:pk>/', Postdetail.as_view()),
    path('user/', Apiviews.as_view())
]