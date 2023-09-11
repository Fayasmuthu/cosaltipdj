from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('index2',views.index2, name='index2'),
    path('index3',views.index3, name='index3'),
    path('index4',views.index4, name='index4'),
    path('service',views.service, name='service'),
    path('project',views.project, name='project'),
    path('blog',views.blog, name='blog'),
    path('contact',views.contact, name='contact'),
    path('project_details',views.project_details, name='project_details'),
    path('blog_details',views.blog_details, name='blog_details'),
    path('Faq',views.faq, name='faq'),
    path('not-found',views.found, name='found'),
    path('service_details',views.service_details, name='service_details'),
    path('team',views.team, name='team'),
    path('dollar',views.dollar, name='dollar'),
    path('gallery',views.gallery, name='gallery'),
    path('tag',views.tag, name='tag'),
    path('search',views.search, name='search'),
    path('paginations',views.paginations, name='paginations'),
    path('form_fields',views.form_fields, name='form_fields'),
    path('success/', views.success, name='success'),
    path('category/<int:category_id>/', views.blog_by_category, name='blog_by_category'),

    # Add more URL patterns here
]
