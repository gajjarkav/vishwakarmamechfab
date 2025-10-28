# Deployment Checklist for VMF Project

## Pre-deployment Steps

### 1. Environment Setup
- [ ] Copy `.env.example` to `.env`
- [ ] Update `DJANGO_SECRET_KEY` with a secure key
- [ ] Set `DJANGO_DEBUG=False`
- [ ] Update `DJANGO_ALLOWED_HOSTS` with your domain

### 2. Database Setup
- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Collect static files: `python manage.py collectstatic`

### 3. Security Settings
- [ ] Change default SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up HTTPS in production
- [ ] Configure CSRF settings if needed

### 4. Static Files
- [ ] Configure web server to serve static files
- [ ] Configure web server to serve media files
- [ ] Ensure proper permissions for media directory

### 5. Admin Panel Access
- [ ] Create admin user account
- [ ] Test admin panel access
- [ ] Verify contact form submissions appear in admin

## Deployment Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (interactive)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Test the application
python manage.py runserver
```

## Production Server Configuration

### Using Gunicorn (Recommended)
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn vmf_project.wsgi:application --bind 0.0.0.0:8000
```

### Nginx Configuration Example
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }
    
    location /media/ {
        alias /path/to/your/project/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Post-deployment Verification

- [ ] Website loads correctly
- [ ] Contact form works and submissions appear in admin
- [ ] Admin panel is accessible
- [ ] Static files (CSS, JS, images) load properly
- [ ] All pages render correctly
- [ ] Gallery and projects sections work
- [ ] Mobile responsiveness is maintained

## Monitoring

- [ ] Set up error logging
- [ ] Monitor contact form submissions
- [ ] Regular database backups
- [ ] Monitor server performance