from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('/bookmarks/', views.bookmark_list, name='bookmark_list'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('bookmark/<int:id>/', views.bookmark_add, name='bookmark_add'),
]
