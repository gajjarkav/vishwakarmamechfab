from django.urls import path
from . import views

app_name = 'vmf_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('projects/', views.projects, name='projects'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('contact/ajax/', views.contact_submit_ajax, name='contact_submit_ajax'),
]
