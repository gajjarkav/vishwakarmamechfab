from django.db import models
from django.utils import timezone

# Create your models here.

class AboutSection(models.Model):
    """Model for managing About Us section content"""
    
    # Main content
    subtitle = models.CharField(
        max_length=200, 
        default="About Vishwakarma Mechfab",
        help_text="Subtitle above the main title"
    )
    title = models.CharField(
        max_length=200, 
        default="Engineering Excellence Since 2010",
        help_text="Main heading of the About section"
    )
    description = models.TextField(
        help_text="Main description paragraph about the company"
    )
    
    # Features
    feature_1_title = models.CharField(
        max_length=100, 
        default="Certified Engineers",
        help_text="Title for first feature"
    )
    feature_1_description = models.TextField(
        default="Licensed professional engineers with extensive industry experience",
        help_text="Description for first feature"
    )
    
    feature_2_title = models.CharField(
        max_length=100, 
        default="Quality Assurance",
        help_text="Title for second feature"
    )
    feature_2_description = models.TextField(
        default="ISO certified processes ensuring highest quality standards",
        help_text="Description for second feature"
    )
    
    feature_3_title = models.CharField(
        max_length=100, 
        default="Latest Technology",
        help_text="Title for third feature"
    )
    feature_3_description = models.TextField(
        default="State-of-the-art tools and software for optimal results",
        help_text="Description for third feature"
    )
    
    # Metadata
    is_active = models.BooleanField(
        default=True,
        help_text="Set to active to display this version on the website"
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"About Section - {self.title}"
    
    def save(self, *args, **kwargs):
        # Ensure only one active instance
        if self.is_active:
            AboutSection.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class Service(models.Model):
    """Model for managing individual service cards"""
    
    # Service details
    title = models.CharField(
        max_length=100,
        help_text="Service title (e.g., 'Design & Engineering')"
    )
    icon = models.CharField(
        max_length=10,
        default="🔧",
        help_text="Emoji icon for the service (e.g., 🔧, 🏭, 💡, 🔍, ⚡, 📊)"
    )
    description = models.TextField(
        help_text="Detailed description of the service"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text="URL-friendly identifier (auto-generated from title)"
    )
    
    # Display settings
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this service from the website"
    )
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which services appear (lower numbers appear first)"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['display_order', 'title']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Project(models.Model):
    """Model for managing project showcase"""
    
    # Project details
    title = models.CharField(
        max_length=200,
        help_text="Project title (e.g., 'Industrial HVAC System')"
    )
    category = models.CharField(
        max_length=100,
        help_text="Project category (e.g., 'Industrial', 'Automotive', 'Energy')"
    )
    short_description = models.TextField(
        max_length=250,
        help_text="Brief description shown on project card (2-3 sentences max)"
    )
    full_description = models.TextField(
        help_text="Detailed description shown in modal/project page"
    )
    
    # Project image
    image_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="External image URL (Cloudinary, etc.) - Leave blank if uploading file"
    )
    image_file = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        help_text="Upload project image directly (recommended)"
    )
    
    # Additional details
    client_name = models.CharField(
        max_length=200,
        blank=True,
        help_text="Client name (optional)"
    )
    completion_date = models.CharField(
        max_length=100,
        blank=True,
        help_text="Completion date (e.g., 'January 2024', optional)"
    )
    location = models.CharField(
        max_length=200,
        blank=True,
        help_text="Project location (optional)"
    )
    
    # SEO and URL
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="URL-friendly identifier (auto-generated from title)"
    )
    
    # Display settings
    is_featured = models.BooleanField(
        default=False,
        help_text="Check to show on homepage (top 3 featured projects appear)"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this project from website"
    )
    display_order = models.IntegerField(
        default=0,
        help_text="Order in which projects appear (lower numbers appear first)"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['display_order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_image_url(self):
        """Return uploaded image URL if available, otherwise external URL"""
        if self.image_file:
            return self.image_file.url
        return self.image_url
    
    def save(self, *args, **kwargs):
        # Auto-generate slug from title if not provided
        if not self.slug:
            from django.utils.text import slugify
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            # Ensure unique slug
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class GalleryItem(models.Model):
    """Model for managing gallery images"""
    
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    
    CATEGORY_CHOICES = [
        ('workshop', 'Workshop'),
        ('fabrication', 'Fabrication'),
        ('welding', 'Welding'),
        ('machinery', 'Machinery'),
        ('projects', 'Projects'),
        ('assembly', 'Assembly'),
        ('testing', 'Testing'),
        ('installation', 'Installation'),
        ('other', 'Other'),
    ]
    
    # Media details
    title = models.CharField(
        max_length=200,
        help_text="Title for the gallery image"
    )
    description = models.TextField(
        max_length=300,
        help_text="Brief description (1-2 sentences)"
    )
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        default='image',
        help_text="Type of media (Image only)"
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='workshop',
        help_text="Category for filtering"
    )
    
    # Media URL/Files
    media_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="External image URL (Cloudinary, etc.) - Leave blank if uploading file"
    )
    media_file = models.FileField(
        upload_to='gallery/',
        blank=True,
        null=True,
        help_text="Upload image file directly (recommended)"
    )
    thumbnail_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Thumbnail URL (optional)"
    )
    thumbnail_file = models.ImageField(
        upload_to='gallery/thumbnails/',
        blank=True,
        null=True,
        help_text="Upload thumbnail (optional)"
    )
    
    # Display settings
    is_featured = models.BooleanField(
        default=False,
        help_text="Show on homepage gallery section (top 2 items)"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this item from gallery"
    )
    display_order = models.IntegerField(
        default=0,
        help_text="Order in gallery (lower numbers appear first)"
    )
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Gallery Item"
        verbose_name_plural = "Gallery Items"
        ordering = ['display_order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_image_url(self):
        """Return uploaded image URL if available, otherwise external URL"""
        if self.media_file:
            return self.media_file.url
        return self.media_url
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ContactInfo(models.Model):
    """Model for managing contact information"""
    
    # Company Details
    company_name = models.CharField(
        max_length=200,
        default="Vishwakarma Mechfab",
        help_text="Company name"
    )
    tagline = models.CharField(
        max_length=200,
        default="Professional mechanical engineering and fabrication solutions for industrial excellence.",
        help_text="Company tagline/description for footer"
    )
    
    # Address Information
    address_line_1 = models.CharField(
        max_length=200,
        default="Industrial Area",
        help_text="Address line 1"
    )
    address_line_2 = models.CharField(
        max_length=200,
        blank=True,
        help_text="Address line 2 (optional)"
    )
    city = models.CharField(
        max_length=100,
        default="Gujarat",
        help_text="City"
    )
    state = models.CharField(
        max_length=100,
        default="Gujarat",
        help_text="State"
    )
    country = models.CharField(
        max_length=100,
        default="India",
        help_text="Country"
    )
    pin_code = models.CharField(
        max_length=20,
        default="123456",
        help_text="PIN/ZIP code"
    )
    
    # Contact Numbers
    primary_phone = models.CharField(
        max_length=20,
        default="+91 98765 43210",
        help_text="Primary phone number"
    )
    secondary_phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Secondary phone number (optional)"
    )
    whatsapp_number = models.CharField(
        max_length=20,
        blank=True,
        help_text="WhatsApp number (optional)"
    )
    
    # Email Addresses
    primary_email = models.EmailField(
        default="info@vishwakarmamechfab.in",
        help_text="Primary email address"
    )
    secondary_email = models.EmailField(
        blank=True,
        help_text="Secondary email address (optional)"
    )
    
    # Website
    website_url = models.URLField(
        default="vishwakarmamechfab.in",
        help_text="Website URL"
    )
    
    # Social Media Links
    facebook_url = models.URLField(
        blank=True,
        help_text="Facebook page URL (optional)"
    )
    instagram_url = models.URLField(
        blank=True,
        help_text="Instagram profile URL (optional)"
    )
    linkedin_url = models.URLField(
        blank=True,
        help_text="LinkedIn profile URL (optional)"
    )
    whatsapp_url = models.URLField(
        blank=True,
        help_text="WhatsApp business URL (optional)"
    )
    twitter_url = models.URLField(
        blank=True,
        help_text="Twitter profile URL (optional)"
    )
    youtube_url = models.URLField(
        blank=True,
        help_text="YouTube channel URL (optional)"
    )
    
    # Working Hours
    working_hours_weekdays = models.CharField(
        max_length=100,
        default="Mon - Sat: 9:00 AM - 6:00 PM",
        help_text="Working hours for weekdays"
    )
    working_hours_weekend = models.CharField(
        max_length=100,
        default="Sunday: Closed",
        help_text="Working hours for weekend"
    )
    
    # Settings
    is_active = models.BooleanField(
        default=True,
        help_text="Set to active to use this contact information"
    )
    
    # Metadata
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"Contact Info - {self.company_name}"
    
    def get_full_address(self):
        """Return formatted full address"""
        address_parts = [
            self.address_line_1,
            self.address_line_2,
            self.city,
            self.state,
            self.country,
            self.pin_code
        ]
        return ", ".join([part for part in address_parts if part])
    
    def save(self, *args, **kwargs):
        # Ensure only one active instance
        if self.is_active:
            ContactInfo.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class ContactSubmission(models.Model):
    """Model for storing contact form submissions"""
    
    # Form Data
    name = models.CharField(
        max_length=200,
        help_text="Sender's name"
    )
    email = models.EmailField(
        help_text="Sender's email address"
    )
    subject = models.CharField(
        max_length=300,
        help_text="Message subject"
    )
    message = models.TextField(
        help_text="Message content"
    )
    
    # Additional Information
    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True,
        help_text="Sender's IP address"
    )
    user_agent = models.TextField(
        blank=True,
        help_text="Sender's browser information"
    )
    
    # Status Management
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('archived', 'Archived'),
    ]
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        help_text="Message status"
    )
    
    admin_notes = models.TextField(
        blank=True,
        help_text="Internal notes (not visible to sender)"
    )
    
    # Timestamps
    submitted_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="When the message was first read"
    )
    replied_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="When the message was replied to"
    )
    
    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.get_status_display()})"
    
    def mark_as_read(self):
        """Mark message as read if it's new"""
        if self.status == 'new':
            self.status = 'read'
            self.read_at = timezone.now()
            self.save()
    
    def mark_as_replied(self):
        """Mark message as replied"""
        self.status = 'replied'
        self.replied_at = timezone.now()
        self.save()
