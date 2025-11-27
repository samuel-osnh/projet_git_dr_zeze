from django.shortcuts import render
from .models import Banner, Page, Section, PageSection, Menu, TeamMember

# -------------------------
# Page d'accueil
# -------------------------
def index(request):
    banners = Banner.objects.all().order_by('-created_at')
    menus = Menu.objects.all().order_by('ordre')
    sections = Section.objects.all()
    team_members = TeamMember.objects.all()

    context = {
        'title': 'TP WEB L3 Info',
        'banners': banners,
        'menus': menus,
        'sections': sections,
        'team_members': team_members,
    }
    return render(request, 'website/index.html', context)

# -------------------------
# Page About
# -------------------------
def about(request):
    about_sections = Section.objects.filter(template='about')
    banners = Banner.objects.all()  # récupère toutes les bannières

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
    team_members = TeamMember.objects.all()
    context = {
        'title': 'Team - TP WEB L3 Info',
        'team_members': team_members,
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