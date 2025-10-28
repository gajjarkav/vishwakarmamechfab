from django.core.management.base import BaseCommand
from vmf_app.models import GalleryItem


class Command(BaseCommand):
    help = 'Populate Gallery with initial data'

    def handle(self, *args, **kwargs):
        # Check if gallery items already exist
        if GalleryItem.objects.exists():
            self.stdout.write(
                self.style.WARNING('Gallery items already exist. Skipping...')
            )
            return

        # Create gallery items
        gallery_data = [
            {
                'title': 'Workshop Operations',
                'description': 'Heavy machinery fabrication in progress at our state-of-the-art facility',
                'media_type': 'image',
                'category': 'workshop',
                'media_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'is_featured': True,
                'is_active': True,
                'display_order': 1
            },
            {
                'title': 'Welding Excellence',
                'description': 'Expert welding and fabrication techniques in action',
                'media_type': 'image',
                'category': 'welding',
                'media_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'is_featured': True,
                'is_active': True,
                'display_order': 2
            },
            {
                'title': 'CNC Machining Process',
                'description': 'Precision cutting and manufacturing with advanced CNC technology',
                'media_type': 'video',
                'category': 'machinery',
                'media_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'thumbnail_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'is_featured': False,
                'is_active': True,
                'display_order': 3
            },
            {
                'title': 'Structural Steel Work',
                'description': 'Large scale structural fabrication and assembly',
                'media_type': 'image',
                'category': 'fabrication',
                'media_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'is_featured': False,
                'is_active': True,
                'display_order': 4
            },
            {
                'title': 'Quality Inspection',
                'description': 'Rigorous quality control and inspection processes',
                'media_type': 'image',
                'category': 'testing',
                'media_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'is_featured': False,
                'is_active': True,
                'display_order': 5
            },
        ]

        created_count = 0
        for item_data in gallery_data:
            item = GalleryItem.objects.create(**item_data)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'✓ Created gallery item: {item.title}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'\n✅ Successfully created {created_count} gallery items!')
        )
