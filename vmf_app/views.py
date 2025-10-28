from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import AboutSection, Service, Project, GalleryItem, ContactInfo, ContactSubmission

# Create your views here.

def index(request):
    """Main homepage view"""
    # Get the active About section, or use first one if none active
    about_section = AboutSection.objects.filter(is_active=True).first()
    if not about_section:
        about_section = AboutSection.objects.first()
    
    # Get all active services, ordered by display_order
    services = Service.objects.filter(is_active=True).order_by('display_order', 'title')
    
    # Get top 3 featured projects for homepage
    featured_projects = Project.objects.filter(
        is_active=True, 
        is_featured=True
    ).order_by('display_order', '-created_at')[:3]
    
    # Get top 2 featured gallery items for homepage
    featured_gallery = GalleryItem.objects.filter(
        is_active=True,
        is_featured=True
    ).order_by('display_order', '-created_at')[:2]
    
    # Get active contact information
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    if not contact_info:
        contact_info = ContactInfo.objects.first()
    
    context = {
        'about_section': about_section,
        'services': services,
        'featured_projects': featured_projects,
        'featured_gallery': featured_gallery,
        'contact_info': contact_info,
    }
    return render(request, 'index.html', context)

def gallery(request):
    """Gallery page view - shows all active gallery images"""
    all_gallery_items = GalleryItem.objects.filter(is_active=True).order_by('display_order', '-created_at')
    
    # Get active contact information
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    if not contact_info:
        contact_info = ContactInfo.objects.first()
    
    context = {
        'gallery_items': all_gallery_items,
        'contact_info': contact_info,
    }
    return render(request, 'gallery.html', context)

def projects(request):
    """Projects page view - shows all active projects"""
    all_projects = Project.objects.filter(is_active=True).order_by('display_order', '-created_at')
    
    # Get active contact information
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    if not contact_info:
        contact_info = ContactInfo.objects.first()
    
    context = {
        'projects': all_projects,
        'contact_info': contact_info,
    }
    return render(request, 'projects.html', context)


@require_POST
def contact_submit(request):
    """Handle contact form submission"""
    try:
        # Get form data
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, subject, message]):
            messages.error(request, 'All fields are required.')
            return redirect('vmf_app:index')
        
        # Get client IP and user agent
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        # Create contact submission
        contact_submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        messages.success(request, 'Thank you for your message! We will get back to you soon.')
        return redirect('vmf_app:index')
        
    except Exception as e:
        messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
        return redirect('vmf_app:index')


@require_POST  
def contact_submit_ajax(request):
    """Handle AJAX contact form submission"""
    try:
        # Parse JSON data
        data = json.loads(request.body)
        
        # Get form data
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'All fields are required.'
            })
        
        # Get client IP and user agent
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        # Create contact submission
        contact_submission = ContactSubmission.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            ip_address=ip_address,
            user_agent=user_agent
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! We will get back to you soon.'
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request format.'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'Sorry, there was an error sending your message. Please try again.'
        })
