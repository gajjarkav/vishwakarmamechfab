from django.core.management.base import BaseCommand
from vmf_app.models import AboutSection


class Command(BaseCommand):
    help = 'Populate the About Section with initial data'

    def handle(self, *args, **kwargs):
        # Check if About section already exists
        if AboutSection.objects.exists():
            self.stdout.write(
                self.style.WARNING('About section already exists. Skipping...')
            )
            return

        # Create the initial About section
        about = AboutSection.objects.create(
            subtitle="About Vishwakarma Mechfab",
            title="Engineering Excellence Since 2010",
            description=(
                "Vishwakarma Mechfab has been at the forefront of mechanical engineering and fabrication "
                "innovation, delivering world-class solutions to industries across India. Our team of "
                "experienced engineers combines traditional engineering principles with modern technology "
                "to solve complex challenges."
            ),
            feature_1_title="Certified Engineers",
            feature_1_description="Licensed professional engineers with extensive industry experience",
            feature_2_title="Quality Assurance",
            feature_2_description="ISO certified processes ensuring highest quality standards",
            feature_3_title="Latest Technology",
            feature_3_description="State-of-the-art tools and software for optimal results",
            is_active=True
        )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created About section: {about.title}')
        )
