#!/usr/bin/env bash
# Build script for Render deployment

set -o errexit  # exit on error

echo "Starting build process..."

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create admin users if they don't exist
echo "Setting up admin users..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()

# Create first admin user (bhavik)
if not User.objects.filter(username='bhavik').exists():
    User.objects.create_superuser('bhavik', 'viswakarmamechfab@gmail.com', 'BhavikKDudhaiya')
    print('✅ Superuser created: bhavik')
else:
    print('✅ Superuser bhavik already exists')

# Create second admin user (kavygajjar)
if not User.objects.filter(username='kavygajjar').exists():
    User.objects.create_superuser('kavygajjar', 'gajjarkav@gmail.com', 'KavyGajjar2024')
    print('✅ Superuser created: kavygajjar')
else:
    print('✅ Superuser kavygajjar already exists')

print('✅ Admin users setup completed')
" || echo "Admin users creation skipped"

echo "✅ Build completed successfully!"