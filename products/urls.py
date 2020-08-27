from django.urls import path
from . import views


urlpatterns = [
    path('wordpress_templates/', views.all_wordpress_templates, name='wordpress_templates'),
    path('wordpress_themes/', views.all_wordpress_themes, name='wordpress_themes'),
    path('squarespace_templates/', views.all_squarespace_templates, name='squarespace_templates'),
    path('squarespace_plugins/', views.all_squarespace_plugins, name='squarespace_plugins'),
]
