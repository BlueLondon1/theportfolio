from django.urls import path

from appfolio import views

urlpatterns = [
    path('', views.welcome, name='index'),
    path('portfolio/', views.welcome, name='portfolio'),
    path('portfolio/detail/<int:pk>/', views.post_detail, name='post-detail'),
    path('portfolio/category/<int:pk>/', views.Category.as_view(), name='post-category-detail'),
    path('portfolio/contact/', views.contactView, name='contact'),
]