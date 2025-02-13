from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostView.as_view(), name='post-list'),
    path('posts/<int:id>/', views.PostView.as_view(), name='post-detail'),
    path('posts/<int:id>/like/', views.LikePostView.as_view(), name='like-post'),
    path('posts/<int:id>/view/', views.ViewPostView.as_view(), name='view-post'),
]