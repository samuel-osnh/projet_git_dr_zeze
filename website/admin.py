from django.contrib import admin
from .models import Page, Section, PageSection, Menu, TeamMember, Banner, ServicesBlock, ParagraphSection, GalleryImage, Slider,SliderLayer,BlockTitle 


# -----------------------
# Admin pour Page
# -----------------------
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'titre', 'description')
    search_fields = ('nom', 'titre')
    

# -----------------------
# Admin pour Section
# -----------------------
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'titre', 'template')
    search_fields = ('nom', 'titre', 'template')

# -----------------------
# Admin pour PageSection
# -----------------------
@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ('page', 'section', 'ordre')
    search_fields = ('page__nom', 'section__nom')
    list_filter = ('page',)

# -----------------------
# Admin pour Menu
# -----------------------
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'parent', 'url', 'ordre')
    search_fields = ('libelle', 'url')
    list_filter = ('parent',)
    ordering = ('ordre',)

# -----------------------
# Admin pour TeamMember
# -----------------------
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')

# -----------------------
# Admin pour Banner
# -----------------------
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    
# ============================
# ADMIN SERVICES BLOCK
# ============================
@admin.register(ServicesBlock)
class ServicesBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'order')
    search_fields = ('title', 'description')
    
# ============================
#   GALLERY IMAGE ADMIN
# ============================
# Inline pour les images associées à un bloc
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    fields = ('image', 'image_name', 'image_subtitle', 'button_text', 'order')
    ordering = ('order',)

# Admin pour BlockTitle
@admin.register(BlockTitle)
class BlockTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'first_title', 'second_title')
    inlines = [GalleryImageInline]
    


# ============================
#   PARAGRAPH SECTION ADMIN
# ============================
@admin.register(ParagraphSection)
class ParagraphSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle_title", "second_title", "name", "job", "order")
    search_fields = ("title", "subtitle_title", "name", "job")
    list_filter = ("order", "daten")
    ordering = ("order",)
    list_editable = ("order",)

    fieldsets = (
        ("Titles", {
            "fields": ("title", "subtitle_title", "second_title")
        }),
        ("Content", {
            "fields": ("description", "message", "vue", "text_button")
        }),
        ("Images", {
            "fields": ("image", "little_image")
        }),
        ("Author / Testimonial", {
            "fields": ("name", "job", "daten")
        }),
        ("Contact & Button", {
            "fields": ("button", "adressage")
        }),
        ("Order", {
            "fields": ("order",)
        }),
    )
# ============================
# ADMIN SLIDER

class SliderLayerInline(admin.TabularInline):
    model = SliderLayer
    extra = 1
    fields = (
        'type_layer',
        'contenu',
        'lien',
        'image',
        'x',
        'y',
        'decalage_vertical',
        'decalage_horizontal',
        'type_animation',
        'duree',
        'delai',
        'ordre',
    )
    ordering = ('ordre',)
    verbose_name = "Calque"
    verbose_name_plural = "Calques"

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'est_actif', 'ordre', 'cree_le')
    list_editable = ('ordre', 'est_actif')
    search_fields = ('titre', 'sous_titre')
    list_filter = ('est_actif',)
    inlines = [SliderLayerInline]

    fieldsets = (
        ("Informations principales", {
            'fields': ('titre', 'sous_titre', 'image', 'video', 'est_actif', 'ordre')
        }),
        ("Paramètres du slide", {
            'fields': ('transition', 'vitesse')
        }),
    )

@admin.register(SliderLayer)
class SliderLayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'slide', 'type_layer', 'ordre', 'type_animation')
    list_editable = ('ordre',)
    search_fields = ('contenu', 'lien')
    list_filter = ('type_layer', 'type_animation')
    ordering = ('ordre',)
