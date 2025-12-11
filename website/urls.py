from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('l3info', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('our-services.html', views.services, name='services'),
    path('services-detail.html', views.services_details, name='services_detail'),
    path('gallery.html', views.gallery, name='gallery'),
    path('team.html', views.team, name='team'),
    path('pricing.html', views.prix, name='pricing'),
    path('blog.html', views.blog, name='blog'),
    path('single-blog-post-left-sidebar.html', views.blog1, name='single_blog_left_sidebar'),
    path('single-blog-post-right-sidebar.html', views.blog2, name='single_blog_right_sidebar'),
    path('single-blog-post-without-sidebar.html', views.blog3, name='single_blog_without_sidebar'),
]