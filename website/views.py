from django.shortcuts import render
from .models import Banner, Page, Section, PageSection, Menu, Slider, BlockTitle, ParagraphSection,ServicesBlock

# -------------------------
# Page d'accueil
# -------------------------
def index(request):
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    

    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    # Récupération des 10 dernières images du bloc Gallery
    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []

    # Récupération des 5 dernières images du bloc Shopping
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()

    
    
    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'since_section': since_section,
        'services_blocks': services_blocks,
        'connect_section': connect_section,

        
    }

    return render(request, 'website/index.html', context)

# -------------------------
# Page About
# -------------------------
def about(request):
    about_sections = Section.objects.filter(template='about')
    banners = Banner.objects.all() # récupère toutes les bannières

    context = {
        'title': 'About - TP WEB L3 Info',
        'about_sections': about_sections,
        'banners': banners,  # on passe les bannières au template
    }
    return render(request, 'website/about.html', context)

# -------------------------
# Page Contact
# -------------------------
def contact(request):
    banners = Banner.objects.all()  # récupère toutes les bannière
    menus = Menu.objects.all().order_by('ordre')
    context = {
        'title': 'Contact - TP WEB L3 Info',
        'menus': menus,
        'banners': banners,  # ici on ajoute les banners au contexte
    }
    return render(request, 'website/contact.html', context)

# -------------------------
# Page Services
# -------------------------
def services(request):
    services_sections = Section.objects.filter(template='services')
    banners = Banner.objects.all()  # récupère toutes les bannière
    context = {
        'title': 'Services - TP WEB L3 Info',
        'services_sections': services_sections,
        'banners': banners,  # ici on ajoute les banners au contexte
    }
    return render(request, 'website/our-services.html', context)

def services_details(request):
    services_details_sections = Section.objects.filter(template='services-detail')
    context = {
        'title': 'Service Detail - TP WEB L3 Info',
        'services_details_sections': services_details_sections,
    }
    return render(request, 'website/services-detail.html', context)

# -------------------------
# Page Gallery
# -------------------------
def gallery(request):
    gallery_sections = Section.objects.filter(template='gallery')
    context = {
        'title': 'Gallery - TP WEB L3 Info',
        'gallery_sections': gallery_sections,
    }
    return render(request, 'website/gallery.html', context)

# -------------------------
# Page Team
# -------------------------
def team(request):
    context = {
        'title': 'Team - TP WEB L3 Info',
    }
    return render(request, 'website/team.html', context)

# -------------------------
# Page Pricing
# -------------------------
def prix(request):
    pricing_sections = Section.objects.filter(template='pricing')
    context = {
        'title': 'Pricing - TP WEB L3 Info',
        'pricing_sections': pricing_sections,
    }
    return render(request, 'website/pricing.html', context)

# -------------------------
# Pages Blog
# -------------------------
def blog(request):
    blog_sections = Section.objects.filter(template='blog')
    context = {
        'title': 'Blog - TP WEB L3 Info',
        'blog_sections': blog_sections,
    }
    return render(request, 'website/blog.html', context)

def blog1(request):
    blog1_sections = Section.objects.filter(template='blog1')
    context = {
        'title': 'Blog Post Left Sidebar - TP WEB L3 Info',
        'blog1_sections': blog1_sections,
    }
    return render(request, 'website/single-blog-post-left-sidebar.html', context)

def blog2(request):
    blog2_sections = Section.objects.filter(template='blog2')
    context = {
        'title': 'Blog Post Right Sidebar - TP WEB L3 Info',
        'blog2_sections': blog2_sections,
    }
    return render(request, 'website/single-blog-post-right-sidebar.html', context)

def blog3(request):
    blog3_sections = Section.objects.filter(template='blog3')
    context = {
        'title': 'Blog Post Without Sidebar - TP WEB L3 Info',
        'blog3_sections': blog3_sections,
    }
    return render(request, 'website/single-blog-post-without-sidebar.html', context)