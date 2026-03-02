from django.core.management.base import BaseCommand
from core.models import Project, Skill
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with sample portfolio data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Seed Skills
        skills_data = [
            {'name': 'Python / Django', 'proficiency': 95},
            {'name': 'JavaScript / React', 'proficiency': 85},
            {'name': 'HTML5 / CSS3', 'proficiency': 90},
            {'name': 'PostgreSQL', 'proficiency': 80},
            {'name': 'Docker', 'proficiency': 75},
        ]
        
        for skill in skills_data:
            Skill.objects.get_or_create(name=skill['name'], defaults={'proficiency': skill['proficiency']})

        # Seed Projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce solution with real-time inventory management and secure payment integration.',
                'tech_stack': 'Django, React, PostgreSQL, Stripe',
                'github_url': 'https://github.com/example/ecommerce',
                'live_url': 'https://example.com/ecommerce',
                'featured': True
            },
            {
                'title': 'Social Media Dashboard',
                'description': 'A comprehensive analytics dashboard for tracking social media engagement and performance across multiple platforms.',
                'tech_stack': 'Python, DRF, Chart.js, Redis',
                'github_url': 'https://github.com/example/dashboard',
                'live_url': 'https://example.com/dashboard',
                'featured': True
            },
            {
                'title': 'AI Content Generator',
                'description': 'An innovative tool that uses GPT models to generate high-quality marketing content and blog posts.',
                'tech_stack': 'Django, OpenAI API, Celery',
                'github_url': 'https://github.com/example/ai-gen',
                'live_url': 'https://example.com/ai-gen',
                'featured': True
            }
        ]

        for p_data in projects_data:
            Project.objects.get_or_create(
                slug=slugify(p_data['title']),
                defaults={
                    'title': p_data['title'],
                    'description': p_data['description'],
                    'tech_stack': p_data['tech_stack'],
                    'github_url': p_data['github_url'],
                    'live_url': p_data['live_url'],
                    'featured': p_data['featured'],
                    'image': 'projects/placeholder.jpg' # Needs manual image upload or fix
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded sample data!'))
