from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.PostView.as_view(), name='post-list'),
    path('posts/<int:id>/', views.PostView.as_view(), name='post-detail'),
    path('posts/<int:id>/like/', views.LikePostView.as_view(), name='like-post'),
    path('posts/<int:id>/view/', views.ViewPostView.as_view(), name='view-post'),
    path('', include('posts.urls')),
]
