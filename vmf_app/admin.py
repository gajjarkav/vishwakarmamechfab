from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import AboutSection, Service, Project, GalleryItem, ContactInfo, ContactSubmission

# Customize Django Admin Site
admin.site.site_header = "Vishwakarma MechFab Administration"
admin.site.site_title = "VMF Admin Portal"
admin.site.index_title = "Welcome to Vishwakarma MechFab Admin Panel"

# Hide Authentication and Authorization section from admin
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    """Admin interface for About Section management"""
    
    list_display = ['title', 'is_active', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    
    fieldsets = (
        ('Main Content', {
            'fields': ('subtitle', 'title', 'description'),
            'description': 'Edit the main About Us section content'
        }),
        ('Feature 1', {
            'fields': ('feature_1_title', 'feature_1_description'),
            'classes': ('collapse',),
        }),
        ('Feature 2', {
            'fields': ('feature_2_title', 'feature_2_description'),
            'classes': ('collapse',),
        }),
        ('Feature 3', {
            'fields': ('feature_3_title', 'feature_3_description'),
            'classes': ('collapse',),
        }),
        ('Settings', {
            'fields': ('is_active',),
            'description': 'Only one About section can be active at a time'
        }),
    )
    
    readonly_fields = []
    
    def get_readonly_fields(self, request, obj=None):
        """Make fields read-only for non-superusers if needed"""
        if obj and not request.user.is_superuser:
            return ['created_at', 'updated_at']
        return self.readonly_fields


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Admin interface for Service management"""
    
    list_display = ['title', 'icon', 'is_active', 'display_order', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'display_order']
    
    def get_prepopulated_fields(self, request, obj=None):
        """Only prepopulate slug for new services"""
        if obj is None:  # Creating new object
            return {'slug': ('title',)}
        return {}
    
    def get_fieldsets(self, request, obj=None):
        """Customize fieldsets based on add vs change"""
        if obj is None:  # Adding new service
            return (
                ('Service Information', {
                    'fields': ('title', 'icon', 'slug'),
                    'description': 'Basic service information. Slug will auto-generate from title.'
                }),
                ('Content', {
                    'fields': ('description',),
                    'description': 'Service description and details'
                }),
                ('Display Settings', {
                    'fields': ('is_active', 'display_order'),
                    'description': 'Control visibility and order of services'
                }),
            )
        else:  # Editing existing service
            return (
                ('Service Information', {
                    'fields': ('title', 'icon', 'slug'),
                    'description': 'Basic service information. Note: Slug cannot be changed after creation.'
                }),
                ('Content', {
                    'fields': ('description',),
                    'description': 'Service description and details'
                }),
                ('Display Settings', {
                    'fields': ('is_active', 'display_order'),
                    'description': 'Control visibility and order of services'
                }),
            )
    
    def get_readonly_fields(self, request, obj=None):
        """Make slug readonly when editing existing service"""
        if obj:  # Editing existing object
            return ['slug']
        return []


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin interface for Project management"""
    
    list_display = ['title', 'category', 'is_featured', 'is_active', 'display_order', 'updated_at']
    list_filter = ['is_featured', 'is_active', 'category', 'created_at']
    search_fields = ['title', 'category', 'short_description', 'client_name']
    list_editable = ['is_featured', 'is_active', 'display_order']
    
    def get_prepopulated_fields(self, request, obj=None):
        """Only prepopulate slug for new projects"""
        if obj is None:  # Creating new object
            return {'slug': ('title',)}
        return {}
    
    def get_fieldsets(self, request, obj=None):
        """Customize fieldsets based on add vs change"""
        if obj is None:  # Adding new project
            return (
                ('Project Information', {
                    'fields': ('title', 'category', 'slug'),
                    'description': 'Basic project information. Slug will auto-generate from title.'
                }),
                ('Project Image', {
                    'fields': ('image_file', 'image_url'),
                    'description': 'Upload image file (recommended) OR provide external image URL'
                }),
                ('Description', {
                    'fields': ('short_description', 'full_description'),
                    'description': 'Short description for card, full description for modal/project page'
                }),
                ('Additional Details (Optional)', {
                    'fields': ('client_name', 'completion_date', 'location'),
                    'classes': ('collapse',),
                }),
                ('Display Settings', {
                    'fields': ('is_featured', 'is_active', 'display_order'),
                    'description': 'Featured projects appear on homepage (top 3). Active projects visible on projects page.'
                }),
            )
        else:  # Editing existing project
            return (
                ('Project Information', {
                    'fields': ('title', 'category', 'slug'),
                    'description': 'Basic project information. Note: Slug cannot be changed after creation.'
                }),
                ('Project Image', {
                    'fields': ('image_file', 'image_url'),
                    'description': 'Upload image file (recommended) OR provide external image URL'
                }),
                ('Description', {
                    'fields': ('short_description', 'full_description'),
                    'description': 'Short description for card, full description for modal/project page'
                }),
                ('Additional Details (Optional)', {
                    'fields': ('client_name', 'completion_date', 'location'),
                    'classes': ('collapse',),
                }),
                ('Display Settings', {
                    'fields': ('is_featured', 'is_active', 'display_order'),
                    'description': 'Featured projects appear on homepage (top 3). Active projects visible on projects page.'
                }),
            )
    
    def get_readonly_fields(self, request, obj=None):
        """Make slug readonly when editing existing project"""
        if obj:  # Editing existing object
            return ['slug']
        return []


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    """Admin interface for Gallery management"""
    
    list_display = ['title', 'category', 'is_featured', 'is_active', 'display_order', 'updated_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured', 'is_active', 'display_order']
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'description', 'category'),
            'description': 'Basic information about the gallery image'
        }),
        ('Image Upload/URL', {
            'fields': ('media_file', 'media_url'),
            'description': 'Upload image file (recommended) OR provide external image URL'
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'display_order'),
            'description': 'Featured items appear on homepage (max 2). Active items visible in gallery.'
        }),
    )
    
    def get_queryset(self, request):
        """Customize queryset"""
        qs = super().get_queryset(request)
        return qs


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """Admin interface for Contact Information management"""
    
    list_display = ['company_name', 'primary_phone', 'primary_email', 'is_active', 'updated_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['company_name', 'primary_phone', 'primary_email']
    
    fieldsets = (
        ('Company Information', {
            'fields': ('company_name', 'tagline'),
            'description': 'Company name and tagline for footer'
        }),
        ('Address Details', {
            'fields': ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'pin_code'),
            'description': 'Complete address information'
        }),
        ('Contact Numbers', {
            'fields': ('primary_phone', 'secondary_phone', 'whatsapp_number'),
            'description': 'Phone numbers and WhatsApp contact'
        }),
        ('Email & Website', {
            'fields': ('primary_email', 'secondary_email', 'website_url'),
            'description': 'Email addresses and website URL'
        }),
        ('Social Media Links', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url', 'whatsapp_url', 'twitter_url', 'youtube_url'),
            'classes': ('collapse',),
            'description': 'Social media profile URLs (optional)'
        }),
        ('Working Hours', {
            'fields': ('working_hours_weekdays', 'working_hours_weekend'),
            'description': 'Business operating hours'
        }),
        ('Settings', {
            'fields': ('is_active',),
            'description': 'Only one contact info can be active at a time'
        }),
    )
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion if it's the only active contact info"""
        if obj and obj.is_active and ContactInfo.objects.filter(is_active=True).count() == 1:
            return False
        return super().has_delete_permission(request, obj)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    """Admin interface for Contact Form Submissions"""
    
    list_display = ['name', 'email', 'subject', 'status', 'submitted_at', 'read_at']
    list_filter = ['status', 'submitted_at', 'read_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['status']
    readonly_fields = ['submitted_at', 'read_at', 'replied_at', 'ip_address', 'user_agent']
    
    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'subject', 'message'),
            'description': 'Contact form submission details'
        }),
        ('Status & Notes', {
            'fields': ('status', 'admin_notes'),
            'description': 'Message status and internal notes'
        }),
        ('Technical Information', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',),
            'description': 'Technical details about the submission'
        }),
        ('Timestamps', {
            'fields': ('submitted_at', 'read_at', 'replied_at'),
            'classes': ('collapse',),
            'description': 'Message timeline'
        }),
    )
    
    def get_queryset(self, request):
        """Mark new messages as read when admin views the list"""
        qs = super().get_queryset(request)
        # Auto-mark messages as read when admin views them
        new_messages = qs.filter(status='new')
        for message in new_messages:
            message.mark_as_read()
        return qs
    
    def has_add_permission(self, request):
        """Disable adding contact submissions from admin (they come from form)"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Allow deletion but show confirmation"""
        return True
    
    def get_actions(self, request):
        """Add custom actions for bulk operations"""
        actions = super().get_actions(request)
        
        def mark_as_read(modeladmin, request, queryset):
            for submission in queryset:
                submission.mark_as_read()
            self.message_user(request, f"{queryset.count()} messages marked as read.")
        mark_as_read.short_description = "Mark selected messages as read"
        
        def mark_as_replied(modeladmin, request, queryset):
            for submission in queryset:
                submission.mark_as_replied()
            self.message_user(request, f"{queryset.count()} messages marked as replied.")
        mark_as_replied.short_description = "Mark selected messages as replied"
        
        def mark_as_archived(modeladmin, request, queryset):
            queryset.update(status='archived')
            self.message_user(request, f"{queryset.count()} messages archived.")
        mark_as_archived.short_description = "Archive selected messages"
        
        actions['mark_as_read'] = (mark_as_read, 'mark_as_read', mark_as_read.short_description)
        actions['mark_as_replied'] = (mark_as_replied, 'mark_as_replied', mark_as_replied.short_description)
        actions['mark_as_archived'] = (mark_as_archived, 'mark_as_archived', mark_as_archived.short_description)
        
        return actions
