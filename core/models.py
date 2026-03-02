from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, help_text="Lucide or FontAwesome icon name")
    proficiency = models.IntegerField(default=80, help_text="Percentage 0-100")
    
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    tech_stack = models.CharField(max_length=200, help_text="Comma separated tags")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [tag.strip() for tag in self.tech_stack.split(',')]
