# Deploy to Render with PostgreSQL

This guide will help you deploy your Django application to Render using PostgreSQL as the database.

## Prerequisites

1. A [Render account](https://render.com)
2. Your code pushed to GitHub repository
3. Basic understanding of environment variables

## Step 1: Create PostgreSQL Database

1. Go to your Render dashboard
2. Click "New" → "PostgreSQL"
3. Configure your database:
   - **Name**: `vishwakarmamechfab-db`
   - **Database**: `vishwakarmamechfab`
   - **User**: `vmf_user`
   - **Plan**: Free (or paid for better performance)
4. Click "Create Database"
5. **Important**: Copy the "External Database URL" - you'll need this later

## Step 2: Create Web Service

1. In Render dashboard, click "New" → "Web Service"
2. Connect your GitHub repository: `https://github.com/gajjarkav/vishwakarmamechfab.git`
3. Configure your web service:

### Basic Settings
- **Name**: `vishwakarmamechfab`
- **Environment**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn vmf_project.wsgi:application`

### Environment Variables
Add these environment variables in the Render dashboard:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.6` |
| `DJANGO_SECRET_KEY` | Generate using: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DJANGO_DEBUG` | `False` |
| `DJANGO_ALLOWED_HOSTS` | `your-app-name.onrender.com` (replace with your actual Render URL) |
| `DATABASE_URL` | Paste the External Database URL from Step 1 |
| `DJANGO_SECURE_SSL_REDIRECT` | `True` |
| `DJANGO_SESSION_COOKIE_SECURE` | `True` |
| `DJANGO_CSRF_COOKIE_SECURE` | `True` |
| `DJANGO_SECURE_HSTS_SECONDS` | `31536000` |
| `DJANGO_ADMIN_URL` | `secure-admin-panel-xyz123/` (customize this for security) |

## Step 3: Deploy

1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Install dependencies from `requirements.txt`
   - Run the build script (`build.sh`)
   - Collect static files
   - Run database migrations
   - Start your application

## Step 4: Post-Deployment Setup

### Create Superuser Account
1. Go to your Render dashboard
2. Navigate to your web service
3. Go to "Shell" tab
4. Run: `python manage.py createsuperuser`
5. Follow the prompts to create your admin account

### Populate Initial Data (Optional)
Run these commands in the Shell to populate your database:
```bash
python manage.py populate_services
python manage.py populate_projects
python manage.py populate_gallery
python manage.py populate_about
```

## Step 5: Access Your Application

- **Website**: `https://your-app-name.onrender.com`
- **Admin Panel**: `https://your-app-name.onrender.com/secure-admin-panel-xyz123/` (use your custom admin URL)

## Important Notes

### Database
- Your PostgreSQL database is automatically backed up by Render
- Free tier databases have limitations (1GB storage, 1 month retention)
- Consider upgrading to paid plan for production use

### Static Files
- Static files are served by WhiteNoise
- Files are automatically compressed and cached
- No additional CDN setup required for basic deployment

### Environment Variables
- Never commit `.env` files to your repository
- Always set environment variables in Render dashboard
- Use strong, unique secret keys for production

### SSL/HTTPS
- Render provides free SSL certificates
- HTTPS is automatically enabled
- Security headers are configured in your Django settings

### Performance
- Free tier has limitations (750 hours/month, sleeps after 15 minutes of inactivity)
- Consider paid plans for production applications
- Monitor your application logs in Render dashboard

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify `build.sh` has correct permissions

### Database Connection Issues
- Verify `DATABASE_URL` is correctly set
- Check PostgreSQL database is running
- Ensure your IP is not blocked (shouldn't be an issue on Render)

### Static Files Not Loading
- Check if `python manage.py collectstatic` runs successfully
- Verify WhiteNoise is properly configured
- Check static file paths in templates

### Application Not Starting
- Check start command: `gunicorn vmf_project.wsgi:application`
- Verify all environment variables are set
- Check application logs for errors

## Monitoring and Maintenance

### Regular Tasks
1. Monitor application logs
2. Check database usage
3. Update dependencies regularly
4. Backup important data
5. Monitor SSL certificate renewal (automatic)

### Scaling
- Upgrade to paid plans for better performance
- Consider adding Redis for caching
- Use CDN for better static file delivery
- Implement proper logging and monitoring

## Support

- [Render Documentation](https://render.com/docs)
- [Django Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/)
- Check application logs for debugging information

## Security Checklist

- ✅ Secret key is secure and unique
- ✅ Debug mode is disabled
- ✅ HTTPS is enabled
- ✅ Security headers are configured
- ✅ Admin URL is customized
- ✅ Database credentials are secure
- ✅ Environment variables are properly set