from django.db import models

# Create your models here.

# website_page
class Page(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la page")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    escription = models.TextField(blank=True)

    # Ajout du ManyToManyField avec le modèle intermédiaire
    sections = models.ManyToManyField(
        'Section',
        through='PageSection',  # Indique le modèle à utiliser pour la relation
        related_name='pages'  # Nom pour la relation inverse (Section.pages)
    )
    class Meta:
        db_table = "page"
        
    def __str__(self):
        return f"Page {self.nom} ({self.titre})"


class Section(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la section")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    template = models.CharField(max_length=255, blank=True, verbose_name="nom de la section sans le html")
    image = models.ImageField( blank=True, null=True, verbose_name="Image de la section")
    
    class Meta:
        db_table = "section"

    def __str__(self):
        return f"Section {self.nom} ({self.titre})"


class PageSection(models.Model):
    # Clé étrangère vers la Page
    page = models.ForeignKey(
        'Page',
        on_delete=models.CASCADE,
        verbose_name="Page hôte"
    )

    # Clé étrangère vers la Section
    section = models.ForeignKey(
        'Section',
        on_delete=models.CASCADE,
        verbose_name="Section incluse"
    )

    # Champ pour l'ordre de la section dans CETTE page
    ordre = models.PositiveIntegerField(
        verbose_name="Ordre dans la page"
    )

    class Meta:
        # S'assurer qu'une page ne peut avoir qu'une seule section à un ordre donné
        unique_together = (('page', 'ordre'), ('page', 'section'),)

        # Définir l'ordre par défaut pour les requêtes sur ce modèle
        ordering = ['ordre']

        # On pourrait aussi ajouter : unique_together = (('page', 'section'),)
        # si une section ne peut apparaître qu'une seule fois par page.
        
        db_table = "page_section"


    def __str__(self):
        return f"Ordre {self.ordre}: {self.section.nom} dans {self.page.nom}"

class Menu(models.Model):
    libelle = models.CharField(max_length=32, verbose_name="Nom de la menu")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Parent menu")
    url = models.CharField(max_length=255, verbose_name="URL de la menu")
    ordre = models.IntegerField(verbose_name="Ordre de la menu")

    def __str__(self):
        return f"Menu {self.libelle} ({self.url})"

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
        ordering = ['ordre']
        unique_together = [['parent', 'ordre']]
        db_table = "menu"



class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')  # sera accessible via MEDIA_URL
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    behance = models.URLField(blank=True, null=True)

    class Meta:
        db_table = "team_member"

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=200)  # pour "About us"
    subtitle = models.CharField(max_length=200, blank=True, null=True)  # pour "faster deliveries"
    background_image = models.ImageField(upload_to='banners/')  # pour l'image de fond
    animation = models.CharField(max_length=50, default='fadeInUp')  # type d'animation
    animation_delay = models.IntegerField(default=200)  # delay en ms
    created_at = models.DateTimeField(auto_now_add=True)  # date de création
    
    class Meta:
        db_table = "banner"

    def __str__(self):
        return self.title

class ServicesBlock(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100) 
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = "services_block"
        ordering = ['order']

    def __str__(self):
        return self.title
    
