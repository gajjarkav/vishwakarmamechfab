from django.core.management.base import BaseCommand
from vmf_app.models import Project


class Command(BaseCommand):
    help = 'Populate Projects with initial data (3 default projects)'

    def handle(self, *args, **kwargs):
        # Check if projects already exist
        if Project.objects.exists():
            self.stdout.write(
                self.style.WARNING('Projects already exist. Skipping...')
            )
            return

        # Create the 3 default projects
        projects_data = [
            {
                'title': 'Industrial HVAC System',
                'category': 'Industrial',
                'short_description': 'Complete HVAC system design and installation for a 50,000 sq ft manufacturing facility',
                'full_description': 'Comprehensive HVAC solution including design, installation, and commissioning for a large-scale manufacturing facility. The project involved custom ductwork fabrication, energy-efficient climate control systems, and advanced automation for optimal performance and reduced operating costs.',
                'image_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'client_name': 'ABC Manufacturing Ltd.',
                'completion_date': 'December 2024',
                'location': 'Gujarat, India',
                'slug': 'industrial-hvac-system',
                'is_featured': True,
                'is_active': True,
                'display_order': 1
            },
            {
                'title': 'Automotive Assembly Line',
                'category': 'Automotive',
                'short_description': 'Automated assembly line optimization resulting in 30% efficiency improvement',
                'full_description': 'Complete overhaul and optimization of automotive assembly line operations. Implementation of automated systems, robotic integration, and process improvements that resulted in significant efficiency gains. The project included custom fabrication of conveyor systems and automated tooling.',
                'image_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'client_name': 'Auto Industries Pvt. Ltd.',
                'completion_date': 'November 2024',
                'location': 'Porbandar, Gujarat',
                'slug': 'automotive-assembly-line',
                'is_featured': True,
                'is_active': True,
                'display_order': 2
            },
            {
                'title': 'Power Plant Maintenance',
                'category': 'Energy',
                'short_description': 'Comprehensive maintenance program for thermal power generation equipment',
                'full_description': 'Ongoing maintenance and support contract for thermal power plant equipment. Services include preventive maintenance, emergency repairs, parts fabrication, and performance optimization. Our team ensures maximum uptime and reliability of critical power generation systems.',
                'image_url': 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
                'client_name': 'Gujarat Power Corporation',
                'completion_date': 'Ongoing',
                'location': 'Gujarat, India',
                'slug': 'power-plant-maintenance',
                'is_featured': True,
                'is_active': True,
                'display_order': 3
            }
        ]

        created_count = 0
        for project_data in projects_data:
            project = Project.objects.create(**project_data)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'✓ Created project: {project.title}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'\n✅ Successfully created {created_count} projects!')
        )
