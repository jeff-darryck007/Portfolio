from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('blog/', views.blog, name='blog'),
    path('blog/<uuid:pk>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.project_list, name='project_list'),
    path('cv/', views.cv, name='cv'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Admin CRUD URLs
    path('manage/projects/', views.AdminProjectListView.as_view(), name='admin_projects'),
    path('manage/projects/create/', views.AdminProjectCreateView.as_view(), name='admin_project_create'),
    path('manage/projects/<uuid:pk>/update/', views.AdminProjectUpdateView.as_view(), name='admin_project_update'),
    path('manage/projects/<uuid:pk>/delete/', views.AdminProjectDeleteView.as_view(), name='admin_project_delete'),

    path('manage/experiences/', views.AdminExperienceListView.as_view(), name='admin_experiences'),
    path('manage/experiences/create/', views.AdminExperienceCreateView.as_view(), name='admin_experience_create'),
    path('manage/experiences/<uuid:pk>/update/', views.AdminExperienceUpdateView.as_view(), name='admin_experience_update'),
    path('manage/experiences/<uuid:pk>/delete/', views.AdminExperienceDeleteView.as_view(), name='admin_experience_delete'),

    path('manage/skills/', views.AdminSkillListView.as_view(), name='admin_skills'),
    path('manage/skills/create/', views.AdminSkillCreateView.as_view(), name='admin_skill_create'),
    path('manage/skills/<uuid:pk>/update/', views.AdminSkillUpdateView.as_view(), name='admin_skill_update'),
    path('manage/skills/<uuid:pk>/delete/', views.AdminSkillDeleteView.as_view(), name='admin_skill_delete'),

    path('manage/categories/', views.AdminCategoryListView.as_view(), name='admin_categories'),
    path('manage/categories/create/', views.AdminCategoryCreateView.as_view(), name='admin_category_create'),
    path('manage/categories/<uuid:pk>/update/', views.AdminCategoryUpdateView.as_view(), name='admin_category_update'),
    path('manage/categories/<uuid:pk>/delete/', views.AdminCategoryDeleteView.as_view(), name='admin_category_delete'),

    path('manage/posts/', views.AdminPostListView.as_view(), name='admin_posts'),
    path('manage/posts/create/', views.AdminPostCreateView.as_view(), name='admin_post_create'),
    path('manage/posts/<uuid:pk>/update/', views.AdminPostUpdateView.as_view(), name='admin_post_update'),
    path('manage/posts/<uuid:pk>/delete/', views.AdminPostDeleteView.as_view(), name='admin_post_delete'),

    path('manage/testimonials/', views.AdminTestimonialListView.as_view(), name='admin_testimonials'),
    path('manage/testimonials/create/', views.AdminTestimonialCreateView.as_view(), name='admin_testimonial_create'),
    path('manage/testimonials/<uuid:pk>/update/', views.AdminTestimonialUpdateView.as_view(), name='admin_testimonial_update'),
    path('manage/testimonials/<uuid:pk>/delete/', views.AdminTestimonialDeleteView.as_view(), name='admin_testimonial_delete'),

    path('manage/contact-messages/', views.AdminContactMessageListView.as_view(), name='admin_contact_messages'),
    path('manage/contact-messages/<uuid:pk>/delete/', views.AdminContactMessageDeleteView.as_view(), name='admin_contact_message_delete'),

    path('manage/settings/', views.AdminCompanySettingListView.as_view(), name='admin_settings'),
    path('manage/settings/<uuid:pk>/update/', views.AdminCompanySettingUpdateView.as_view(), name='admin_setting_update'),
    # Secret Login
    path('jeff-admin-login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
