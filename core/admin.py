from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    Category, Service, Skill, Project, 
    Experience, Testimonial, CompanySetting,
    Tag, Post, ContactMessage
)




class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'modified')
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ('name', 'slug', 'is_active')
    exclude = ('slug',)
    prepopulated_fields = {'slug': ('name',)}  # keeps automatic behavior if field ever shown

@admin.register(Service)
class ServiceAdmin(BaseAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(Skill)
class SkillAdmin(BaseAdmin):
    list_display = ('name', 'proficiency', 'category', 'is_active')
    list_filter = ('category', 'is_active')

@admin.register(Project)
class ProjectAdmin(BaseAdmin):
    list_display = ('title', 'category', 'featured', 'is_active', 'created')
    exclude = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'tech_stack')
    list_filter = ('category', 'featured', 'is_active', 'created')

@admin.register(Experience)
class ExperienceAdmin(BaseAdmin):
    list_display = ('position', 'company', 'start_date', 'is_current', 'is_active')
    list_filter = ('is_current', 'is_active')
    search_fields = ('position', 'company')

@admin.register(Testimonial)
class TestimonialAdmin(BaseAdmin):
    list_display = ('name', 'position', 'is_active')

@admin.register(CompanySetting)
class CompanySettingAdmin(BaseAdmin):
    fieldsets = (
        (_("General Info"), {
            'fields': ('name', 'logo', 'favicon', 'email', 'phone', 'address')
        }),
        (_("Social Links"), {
            'fields': ('linkedin', 'github', 'twitter', 'instagram')
        }),
        (_("Bio & Documents"), {
            'fields': ('bio_title', 'bio_text', 'cv_file')
        }),
        (_("Meta"), {
            'fields': ('author', 'is_active', 'is_deleted', 'created', 'modified'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        if CompanySetting.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Tag)
class TagAdmin(BaseAdmin):
    list_display = ('name', 'slug', 'is_active')
    exclude = ('slug',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(BaseAdmin):
    list_display = ('title', 'is_published', 'published_date', 'is_active')
    list_filter = ('is_published', 'is_active', 'tags')
    exclude = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)

@admin.register(ContactMessage)
class ContactMessageAdmin(BaseAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created')
    list_filter = ('is_read', 'created')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('id', 'name', 'email', 'subject', 'message', 'author', 'created', 'modified')
    list_editable = ('is_read',)

    def has_add_permission(self, request):
        return False



