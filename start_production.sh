#!/bin/bash
# Production startup script for Vishwakarma Mechfab

echo "🚀 Starting Vishwakarma Mechfab production deployment..."

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
    echo "✅ Environment variables loaded"
else
    echo "❌ .env file not found!"
    exit 1
fi

# Activate virtual environment (if using)
# source venv/bin/activate

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🔄 Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if needed (interactive)
echo "👤 Create superuser if needed..."
python manage.py shell -c "
from django.contrib.auth.models import User;
if not User.objects.filter(is_superuser=True).exists():
    print('No superuser found. Please create one:')
    import subprocess
    subprocess.call(['python', 'manage.py', 'createsuperuser'])
"

# Start production server
echo "🌐 Starting production server..."
echo "Admin panel will be available at: https://vishwakarmamechfab.in/$DJANGO_ADMIN_URL"

# Use Gunicorn for production
gunicorn vmf_project.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120 \
    --max-requests 1000 \
    --preload \
    --access-logfile logs/access.log \
    --error-logfile logs/error.log \
    --log-level info

echo "🎉 Vishwakarma Mechfab is now running!"
