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
    def __str__(self):
        return f"Page {self.nom} ({self.titre})"


class Section(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la section")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)

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


from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')  # sera accessible via MEDIA_URL
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    behance = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# python manage.py makemigrations