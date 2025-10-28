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

print('=== ADMIN USERS SETUP ===')

# Create first admin user (bhavikgajjar)
if not User.objects.filter(username='bhavikgajjar').exists():
    user1 = User.objects.create_superuser('bhavikgajjar', 'viswakarmamechfab@gmail.com', 'BhavikKDudhaiya')
    print('✅ Superuser created: bhavikgajjar')
    print(f'   Email: {user1.email}')
    print(f'   Password: BhavikKDudhaiya')
else:
    print('✅ Superuser bhavikgajjar already exists')

# Create second admin user (kavygajjar)
if not User.objects.filter(username='kavygajjar').exists():
    user2 = User.objects.create_superuser('kavygajjar', 'gajjarkav@gmail.com', 'KavyGajjar1')
    print('✅ Superuser created: kavygajjar')
    print(f'   Email: {user2.email}')
    print(f'   Password: KavyGajjar1')
else:
    print('✅ Superuser kavygajjar already exists')

print('\n=== FINAL ADMIN USERS LIST ===')
superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    print(f'Username: {user.username} | Email: {user.email} | Active: {user.is_active}')

print(f'\nTotal admin users: {superusers.count()}')
print('=== END ADMIN SETUP ===')
" || echo "Admin users creation skipped"

echo "✅ Build completed successfully!"