from django.db import models
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

# website_page
class Page(models.Model):
    nom = models.CharField(max_length=32, verbose_name="Nom de la page")
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)

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




    class Meta:
        db_table = "team_member"
        ordering = ['id']

    def __str__(self):
        return self.name


class Banner(models.Model):
    ANIMATION_CHOICES = [
        ('fadeIn', 'Fade In'),
        ('fadeInUp', 'Fade In Up'),
        ('zoomIn', 'Zoom In'),
        ('bounceIn', 'Bounce In'),
        ('none', 'Aucune animation'),
    ]

    DELAY_CHOICES = [
        ('0s', '0 seconde'),
        ('0.5s', '0.5 seconde'),
        ('1s', '1 seconde'),
        ('1.5s', '1.5 seconde'),
        ('2s', '2 secondes'),
    ]

    title = models.CharField(max_length=200, default="Titre")
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    animation = models.CharField(max_length=20, choices=ANIMATION_CHOICES, default='fadeIn')
    animation_delay = models.CharField(max_length=5, choices=DELAY_CHOICES, default='0s')
    cree_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "banner"

    def __str__(self):
        return self.title

    
# Gère les blocks de services (icon ou il y'a le smill)
class ServicesBlock(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(
        upload_to='paragraph_sections/icons/', 
        blank=True, 
        null=True,
        help_text="Icône associée à la section"
    )
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = "services_block"
        ordering = ['order']

    def __str__(self):
        return self.title
    
# Gère  start shuppig with us, our galery et awards

# Modèle pour le bloc Gallery (titre + sous-titre + description)
class BlockTitle(models.Model):
    SECTION_CHOICES = [
        ('awards', 'Awards'),
        ('gallery', 'Our Gallery'),
        ('shopping', 'Start Shopping With Us'),
    ]

    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='awards', blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True, help_text="Titre de la section")
    first_title = models.CharField(max_length=200, blank=True, null=True, help_text="Sous-titre")
    second_title = models.CharField(max_length=200, blank=True, null=True, help_text="Petite description")

    class Meta:
        db_table = "block_title"

    def __str__(self):
        return self.title if self.title else f"Block {self.id}"


# Modèle pour chaque image associée à un bloc
class GalleryImage(models.Model):
    block = models.ForeignKey(BlockTitle, on_delete=models.CASCADE, related_name='images', default=1)
    image = models.ImageField(upload_to='gallery/')
    image_name = models.CharField(max_length=255, blank=True, null=True, help_text="Nom sur l'image")
    image_subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Sous-titre sur l'image")
    button_text = models.CharField(max_length=100, blank=True, null=True, help_text="Bouton sur l'image")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "gallery_image"
        ordering = ['order']

    def __str__(self):
        return self.image_name if self.image_name else f"Image {self.id}"



class ParagraphSection(models.Model):
    SECTION_CHOICES = [
        ('since', 'Since'),
        ('connect', 'Connect'),
        
    ]

    section_type = models.CharField(
        max_length=20, 
        choices=SECTION_CHOICES, 
        default='since',
        help_text="Choisir le type de section"
    )

    title = models.CharField(max_length=200)
    subtitle_title = models.CharField(max_length=200, blank=True, null=True)
    second_title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='paragraph_sections/', blank=True, null=True)
    little_image = models.ImageField(upload_to='paragraph_sections/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    daten = models.DateTimeField(blank=True, null=True)
    message = models.IntegerField(blank=True, null=True)
    vue = models.CharField(max_length=5, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    button = models.CharField(max_length=100, blank=True, null=True)
    adressage = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=True, null=True)
    text_button = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.section_type})"

    
    class Meta:
        db_table = "paragraphe_section"
        ordering = ['order']

    def __str__(self):
        return self.title
    


class Slider(models.Model):
    # Slide principal
    titre = models.CharField(max_length=255, blank=True, null=True)
    sous_titre = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sliders/', blank=True, null=True)
    video = models.FileField(upload_to='sliders/videos/', blank=True, null=True)
    est_actif = models.BooleanField(default=True)
    ordre = models.PositiveIntegerField(default=0)

    # Paramètres du slide
    transition = models.CharField(
        max_length=50,
        choices=[
            ('fade', 'Fondu'),
            ('zoomout', 'Zoom arrière'),
            ('slideleft', 'Glisser à gauche'),
            ('slideright', 'Glisser à droite'),
        ],
        default='fade'
    )
    vitesse = models.PositiveIntegerField(default=1500, help_text="Durée de la transition du slide en millisecondes (ex: 2000 = 2 secondes).")

    cree_le = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['ordre']
        verbose_name = "Slide"
        verbose_name_plural = "Slides"

    def __str__(self):
        return f"Slide {self.id} - {self.titre or 'Sans titre'}"


class SliderLayer(models.Model):
    slide = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='layers')

    # Type de layer
    TYPES_LAYER = [
        ('text', 'Texte (Titre, paragraphe'),
        ('button', 'Bouton (Lien cliquable)'),
        ('shape', 'Forme (Arrière-plan, couleur)'),
    ]
    type_layer = models.CharField(max_length=20, choices=TYPES_LAYER, default='text')

    contenu = models.TextField(blank=True, null=True,verbose_name="Texte Affiché", help_text="Le contenu du calque (texte du titre ou étiquette du bouton")
    lien = models.URLField(blank=True, null=True, verbose_name="Lien Cliquable (URL)", help_text="L'adresse vers laquelle le calque redirige (pour les boutons)." )
    image = models.ImageField(upload_to='slider_layers/', blank=True, null=True)

    # Positionnement simple pour l'admin
    x = models.CharField(max_length=50, default='center', choices=[('left', 'Gauche'), ('center', 'Centre'), ('right', 'Droite')], verbose_name="Alignement Horizontal (centre l'élément)")
    y = models.CharField(max_length=50, default='middle', choices=[('top', 'Haut'), ('middle', 'Milieu'), ('bottom', 'Bas')], verbose_name="Alignement Vertical (centre l'élément)")
    
    # 2. Décalage par rapport à l'alignement
    decalage_horizontal = models.IntegerField(default=0, help_text="Déplacement en pixels par rapport à l'alignement X. Positif pour aller à droite, négatif pour aller à gauche.")
    decalage_vertical = models.IntegerField(default=0, help_text="Déplacement en pixels par rapport à l'alignement Y. Utilisez un nombre négatif (ex: -70) pour monter, positif (ex: 50) pour descendre. C'est essentiel pour empiler les éléments !")

    # Animation simple
    type_animation = models.CharField(
        max_length=50,
        choices=[
            ('fade', 'Fondu'),
            ('fade-up', 'Fondu vers le haut'),
            ('fade-down', 'Fondu vers le bas'),
            ('slide-left', 'Glisser à gauche'),
            ('slide-right', 'Glisser à droite'),
            ('zoom-in', 'Zoom avant'),
        ],
        default='fade'
    )
    duree = models.PositiveIntegerField(default=2000, validators=[MinValueValidator(100)], help_text="Durée de l'animation d'entrée en millisecondes.")
    
    delai = models.PositiveIntegerField(default=1000, validators=[MinValueValidator(100)], help_text="Temps en ms (millisecondes) avant que le calque n'apparaisse (1000 = 1 seconde).")

    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordre']

    def __str__(self):
        return f"Layer {self.type_layer} pour slide {self.slide.id}"

from django.db import models

# -----------------------------
# Titre de section
# -----------------------------
class TitleSection(models.Model):
    SECTION_CHOICES = [
        ('testimonials', 'Testimonials'),
        ('cheap_pricing', 'Cheap Pricing'),
        ('our_team', 'Our Team'),
        ('savor_savings', 'Savor the Savings'),
        ('stay_informed', 'Stay Informed'),
    ]

    section_type = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        default='testimonials',
        help_text="Choisir le type de section"
    )
    title = models.CharField(max_length=200, help_text="Titre principal")
    subtitle = models.CharField(max_length=200, blank=True, null=True, help_text="Sous-titre")
    description = models.TextField(blank=True, null=True, help_text="Description longue")
    image = models.ImageField(upload_to='image/',null=True, blank=True) # accessible via MEDIA_URL

    class Meta:
        verbose_name = "Section Titre"
        verbose_name_plural = "Sections Titre"

    def __str__(self):
        return self.title


# -----------------------------
# Paragraphe lié à une section
# -----------------------------
class ParagraphTitleAndManyElement(models.Model):
    section = models.ForeignKey(
        TitleSection,  # lien vers TitleSection
        on_delete=models.CASCADE,
        related_name='elements',
        help_text="Choisir la section à laquelle ce paragraphe appartient"
    )
    description_carrouselle = models.TextField(blank=True, null=True, help_text="Description pour le commentaire defilnt")
    name = models.CharField(max_length=200, default="Texte par défaut")
    job = models.CharField(max_length=200, default="Texte par défaut",null=True, blank=True)
    adresse = models.CharField(max_length=20, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    image_caroussel = models.ImageField(upload_to='image/',blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    behance = models.URLField(blank=True, null=True)
    button = models.CharField(max_length=100, blank=True, null=True, help_text="Texte du bouton principal")
    button_text = models.TextField( blank=True, null=True, help_text="Texte supplémentaire du bouton")
    montant = models.IntegerField(blank=True, null=True)
    avantage_prix = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=True, null=True, help_text="Ordre d'affichage")

    class Meta:
        ordering = ['order']
        verbose_name = "Paragraph Title & Element"
        verbose_name_plural = "Paragraph Titles & Elements"

