from django.contrib import admin
from .models import Page, Section, PageSection, Menu, TeamMember, Banner, ServicesBlock

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
    list_display = ('title', 'subtitle', 'animation', 'animation_delay', 'created_at')
    search_fields = ('title', 'subtitle')
    
@admin.register(ServicesBlock)
class ServicesBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'order')
    search_fields = ('title', 'description')