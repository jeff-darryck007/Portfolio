from django.urls import path
from django.contrib.auth import views as auth_views
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

    # Admin CRUD URLs
    path('admin/projects/', views.AdminProjectListView.as_view(), name='admin_projects'),
    path('admin/experiences/', views.AdminExperienceListView.as_view(), name='admin_experiences'),
    path('admin/skills/', views.AdminSkillListView.as_view(), name='admin_skills'),
    path('admin/categories/', views.AdminCategoryListView.as_view(), name='admin_categories'),
    path('admin/posts/', views.AdminPostListView.as_view(), name='admin_posts'),
    path('admin/testimonials/', views.AdminTestimonialListView.as_view(), name='admin_testimonials'),
    path('admin/contact-messages/', views.AdminContactMessageListView.as_view(), name='admin_contact_messages'),
    path('admin/settings/', views.AdminCompanySettingListView.as_view(), name='admin_settings'),

    # Secret Login
    path('jeff-admin-login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
