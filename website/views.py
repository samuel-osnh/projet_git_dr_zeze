from django.shortcuts import render
from .models import Banner, Page, Section, PageSection, Menu, Slider, BlockTitle, ParagraphSection,ServicesBlock

from django.shortcuts import render
from .models import (
    Banner, Menu, Section, Slider, 
    ParagraphSection, TitleSection, ParagraphTitleAndManyElement,
    BlockTitle, ServicesBlock
)

def index(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

    }

    return render(request, 'website/index.html', context)


# -------------------------
# Page About
# -------------------------
def about(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

    }
    return render(request, 'website/about.html', context)

# -------------------------
# Page Contact
# -------------------------
def contact(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

    }
    return render(request, 'website/contact.html', context)

# -------------------------
# Page Services
# -------------------------
def services(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

    }
    return render(request, 'website/our-services.html', context)

def services_details(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

    }
    return render(request, 'website/services-detail.html', context)

# -------------------------
# Page Gallery
# -------------------------
def gallery(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

    }
    return render(request, 'website/gallery.html', context)

# -------------------------
# Page Team
# -------------------------
def team(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

    }
    return render(request, 'website/team.html', context)

# -------------------------
# Page Pricing
# -------------------------
def prix(request):
    # Bannières et menus
    banners = Banner.objects.all().order_by('cree_le')
    menus = Menu.objects.all().order_by('ordre')
    
    # Sections classiques
    sections = Section.objects.all()
    slides = Slider.objects.filter(est_actif=True)
    
    # Sections dynamiques ParagraphSection
    since_section = ParagraphSection.objects.filter(section_type='since').first()
    connect_section = ParagraphSection.objects.filter(section_type='connect').first()
    
    # Sections dynamiques TitleSection
    title_sections = TitleSection.objects.all().prefetch_related('elements')  # récupère les ParagraphTitleAndManyElement liés

    # Blocs spécifiques
    awards_block = BlockTitle.objects.filter(section='awards').first()
    gallery_block = BlockTitle.objects.filter(section='gallery').first()
    shopping_block = BlockTitle.objects.filter(section='shopping').first()

    gallery_images = gallery_block.images.all().order_by('-id')[:10] if gallery_block else []
    shopping_images = shopping_block.images.all().order_by('-id')[:5] if shopping_block else []
        # Récupération de la section "Savor the Savings"
    savor_section = TitleSection.objects.filter(title="Savor the Savings").first()
    features_elements = savor_section.elements.all() if savor_section else []
    
    testimonial_section = TitleSection.objects.filter(section_type='testimonials').first()
    testimonials = testimonial_section.elements.all() if testimonial_section else []

    services_blocks = ServicesBlock.objects.order_by('order')[:3]
    
    pricing_section = TitleSection.objects.filter(section_type="cheap_pricing").first()
    pricing_items = ParagraphTitleAndManyElement.objects.filter(section=pricing_section).order_by('order') if pricing_section else []


    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'sliders': slides,
        'since_section': since_section,
        'connect_section': connect_section,
        'title_sections': title_sections,
        'awards_block': awards_block,
        'gallery_block': gallery_block,
        'shopping_block': shopping_block,
        'gallery_images': gallery_images,
        'shopping_images': shopping_images,
        'services_blocks': services_blocks,
        'savor_section': savor_section,
        'features_elements': features_elements,
        'testimonial_section': testimonial_section,
        'testimonials': testimonials,
        'pricing_section': pricing_section,
        'pricing_items': pricing_items,

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