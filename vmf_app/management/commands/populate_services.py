from django.core.management.base import BaseCommand
from vmf_app.models import Service


class Command(BaseCommand):
    help = 'Populate the Services with initial data (6 default services)'

    def handle(self, *args, **kwargs):
        # Check if services already exist
        if Service.objects.exists():
            self.stdout.write(
                self.style.WARNING('Services already exist. Skipping...')
            )
            return

        # Create the 6 default services
        services_data = [
            {
                'title': 'Design & Engineering',
                'icon': '🔧',
                'description': 'Custom mechanical design solutions from concept to completion, including 3D modeling, CAD drawings, and technical specifications.',
                'slug': 'design-engineering',
                'display_order': 1
            },
            {
                'title': 'Manufacturing Solutions',
                'icon': '🏭',
                'description': 'End-to-end manufacturing support including process optimization, quality control, and production planning for efficient operations.',
                'slug': 'manufacturing-solutions',
                'display_order': 2
            },
            {
                'title': 'Consulting Services',
                'icon': '💡',
                'description': 'Expert consulting for project planning, feasibility studies, technical audits, and engineering optimization strategies.',
                'slug': 'consulting-services',
                'display_order': 3
            },
            {
                'title': 'Maintenance & Support',
                'icon': '🔍',
                'description': 'Preventive maintenance programs, troubleshooting, and ongoing technical support to ensure optimal equipment performance.',
                'slug': 'maintenance-support',
                'display_order': 4
            },
            {
                'title': 'Automation Solutions',
                'icon': '⚡',
                'description': 'Industrial automation design and implementation to improve efficiency, reduce costs, and enhance productivity.',
                'slug': 'automation-solutions',
                'display_order': 5
            },
            {
                'title': 'Analysis & Testing',
                'icon': '📊',
                'description': 'Comprehensive analysis including stress testing, thermal analysis, and performance evaluation for optimal design validation.',
                'slug': 'analysis-testing',
                'display_order': 6
            }
        ]

        created_count = 0
        for service_data in services_data:
            service = Service.objects.create(**service_data)
            created_count += 1
            self.stdout.write(
                self.style.SUCCESS(f'✓ Created service: {service.title}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'\n✅ Successfully created {created_count} services!')
        )
