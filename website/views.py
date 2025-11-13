# tp3/website/views.py
from django.shortcuts import render

def index(request):
    context = {
        'title': 'TP WEB L3 Info',
        'about': get_about()
    }
    return render(request, 'website/index.html', context)

def about(request):

    context = {
        'title': 'TP WEB L3 Info',
        'about': get_about()
    }
    return render(request, 'website/about.html', context)

def contact(request):
    return render(request, 'website/contact.html')

def services(request):
    return render(request, 'website/our-services.html')

def services_details(request):
    return render(request, 'website/services-detail.html')

def gallery(request):
    return render(request, 'website/gallery.html')

def team(request):
    return render(request, 'website/team.html')

def prix(request):
    return render(request, 'website/pricing.html')

def blog(request):
    return render(request, 'website/blog.html')

def blog1(request):
    return render(request, 'website/single-blog-post-left-sidebar.html')

def blog2(request):
    return render(request, 'website/single-blog-post-right-sidebar.html')

def blog3(request):
    return render(request, 'website/single-blog-post-without-sidebar.html')

def get_about():
    data = {
        'section_title': 'Since 1998',
        'about_title': 'Making transportation fast and safe',
        'description': """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            lorem Ipsum has been the industry standard dummy text ever since 
            the when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book.
        """,
        'about_author': 'Toto Titi',
        'about_fonction': "Directeur General",
        'about_service':[
            {
                'img':'1.svg',
                'title':'Fast Deliver',
                'description':'Lorem Ipsum',
                'order':1,
            },
            {
                'img':'1.svg',
                'title':'100% Satifaction',
                'description':'Lorem Ipsum',
                'order':2,
            },
            {
                'img':'3.svg',
                'title':'24x7 Service',
                'description':'Lorem Ipsum',
                'order':3,
            },
        ]
    }
    return data

