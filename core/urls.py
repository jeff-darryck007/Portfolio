from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.project_list, name='project_list'),
    path('cv/', views.cv, name='cv'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
