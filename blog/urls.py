from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(),name='blog-home'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),
    path('create/new', views.CreatePotView.as_view(),name='post-create'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(),name='post-update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>/', views.UserPostListView.as_view(),name='user-post'),
    path('about/', views.about,name='blog-about'),
]