import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    'created' and 'modified' fields.
    """
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_("Créé le"))
    modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_("Modifié le"))

    class Meta:
        abstract = True

class ActivatorModel(models.Model):
    """
    An abstract base class model that provides an 'is_active' field.
    """
    is_active = models.BooleanField(default=True, verbose_name=_("Actif"))

    class Meta:
        abstract = True

class BaseModel(TimeStampedModel, ActivatorModel):
    """
    Modèle de base abstrait pour toutes les entités LEINAD.
    Fournit : created/modified (TimeStampedModel) + is_active (ActivatorModel)
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("Identifiant"),
    )
    is_deleted = models.BooleanField(
        default=False, verbose_name=_("Supprimé logiquement")
    )

    author = models.ForeignKey(
        "auth.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created_by",
        verbose_name=_("Auteur"),
    )

    class Meta:
        abstract = True
        ordering = ["-created"]

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id})"

    def soft_delete(self):
        self.is_deleted = True
        self.save(update_fields=["is_deleted"])

class Category(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Nom"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Catégorie")
        verbose_name_plural = _("Catégories")

    def __str__(self):
        return self.name

class Service(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Titre"))
    description = models.TextField(verbose_name=_("Description"))
    icon = models.CharField(max_length=50, help_text=_("Nom de l'icône (Lucide, Lucide, FontAwesome)"), verbose_name=_("Icône"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Ordre d'affichage"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ["order", "-created"]

    def __str__(self):
        return self.title

class Skill(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("Nom"))
    icon = models.CharField(max_length=50, help_text=_("Lucide or FontAwesome icon name"), verbose_name=_("Icône"))
    proficiency = models.IntegerField(default=80, help_text=_("Percentage 0-100"), verbose_name=_("Maîtrise"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="skills", null=True, blank=True, verbose_name=_("Catégorie"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Compétence")
        verbose_name_plural = _("Compétences")

    def __str__(self):
        return self.name

class Project(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Titre"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to='projects/', verbose_name=_("Image"))
    tech_stack = models.CharField(max_length=200, help_text=_("Comma separated tags"), verbose_name=_("Technologies"))
    github_url = models.URLField(blank=True, verbose_name=_("URL GitHub"))
    live_url = models.URLField(blank=True, verbose_name=_("URL Live"))
    featured = models.BooleanField(default=False, verbose_name=_("Mis en avant"))
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="projects", verbose_name=_("Catégorie"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Projet")
        verbose_name_plural = _("Projets")

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [tag.strip() for tag in self.tech_stack.split(',')]

class Experience(BaseModel):
    company = models.CharField(max_length=200, verbose_name=_("Entreprise"))
    position = models.CharField(max_length=200, verbose_name=_("Poste"))
    location = models.CharField(max_length=200, blank=True, verbose_name=_("Lieu"))
    start_date = models.DateField(verbose_name=_("Date de début"))
    end_date = models.DateField(null=True, blank=True, verbose_name=_("Date de fin"))
    is_current = models.BooleanField(default=False, verbose_name=_("Poste actuel"))
    description = models.TextField(verbose_name=_("Description"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Expérience")
        verbose_name_plural = _("Expériences")
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} @ {self.company}"

class Testimonial(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Nom"))
    position = models.CharField(max_length=100, verbose_name=_("Poste/Entreprise"))
    content = models.TextField(verbose_name=_("Contenu"))
    avatar = models.ImageField(upload_to='testimonials/', null=True, blank=True, verbose_name=_("Avatar"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Témoignage")
        verbose_name_plural = _("Témoignages")

    def __str__(self):
        return f"Témoignage de {self.name}"

class CompanySetting(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("Nom du site/entreprise"))
    logo = models.ImageField(upload_to='settings/', verbose_name=_("Logo"))
    favicon = models.ImageField(upload_to='settings/', null=True, blank=True, verbose_name=_("Favicon"))
    email = models.EmailField(verbose_name=_("Email de contact"))
    phone = models.CharField(max_length=20, blank=True, verbose_name=_("Téléphone"))
    address = models.TextField(blank=True, verbose_name=_("Adresse"))
    
    # Social Links
    linkedin = models.URLField(blank=True, verbose_name=_("LinkedIn"))
    github = models.URLField(blank=True, verbose_name=_("GitHub"))
    twitter = models.URLField(blank=True, verbose_name=_("Twitter/X"))
    instagram = models.URLField(blank=True, verbose_name=_("Instagram"))

    # About Summary
    bio_title = models.CharField(max_length=200, blank=True, verbose_name=_("Titre Bio"))
    bio_text = models.TextField(blank=True, verbose_name=_("Texte Bio"))
    cv_file = models.FileField(upload_to='documents/', null=True, blank=True, verbose_name=_("Curriculum Vitae"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Paramètre du site")
        verbose_name_plural = _("Paramètres du site")

    def __str__(self):
        return f"Configuration de {self.name}"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and CompanySetting.objects.exists():
            # You can either raise an error or return existing
            return
        return super().save(*args, **kwargs)

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Nom"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name

class Post(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Titre"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug"))
    featured_image = models.ImageField(upload_to='blog/', verbose_name=_("Image mise en avant"))
    content = models.TextField(verbose_name=_("Contenu"))
    excerpt = models.TextField(blank=True, verbose_name=_("Extrait"))
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True, verbose_name=_("Tags"))
    
    published_date = models.DateTimeField(null=True, blank=True, verbose_name=_("Date de publication"))
    is_published = models.BooleanField(default=False, verbose_name=_("Publié"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_date:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)

class ContactMessage(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Nom"))
    email = models.EmailField(verbose_name=_("Email"))
    subject = models.CharField(max_length=200, verbose_name=_("Sujet"))
    message = models.TextField(verbose_name=_("Message"))
    is_read = models.BooleanField(default=False, verbose_name=_("Lu"))

    class Meta(BaseModel.Meta):
        verbose_name = _("Message de contact")
        verbose_name_plural = _("Messages de contact")

    def __str__(self):
        return f"Message de {self.name} - {self.subject}"



