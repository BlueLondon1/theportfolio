from django.urls import path

from appfolio import views

urlpatterns = [
    path('portfolio/', views.welcome, name='portfolio'),
    path('portfolio/articles/', views.articleView, name='articles'),
    path('portfolio/contact/', views.contactView, name='contact'),
    path('portfolio/success/', views.successView, name='success'),
    path('portfolio/test/', views.test, name='test'),
]