# Deploy Your Django App to Render (Using Your Existing Database)

Your PostgreSQL database is already created! Here's how to deploy your Django web application.

## 🗄️ Your Database Details (Already Created)
- **Database Name**: `vishwakarmamechfab`
- **Region**: Singapore (Southeast Asia)
- **Status**: Available ✅
- **Internal URL**: `postgresql://kavygajjar:r0gYmyGlFRashWZ1lfznAo0CMFxdP1ZA@dpg-d4087tpr0fns73bhngfg-a/maindb_4rsy`
- **External URL**: `postgresql://kavygajjar:r0gYmyGlFRashWZ1lfznAo0CMFxdP1ZA@dpg-d4087tpr0fns73bhngfg-a.singapore-postgres.render.com/maindb_4rsy`

## 🚀 Step 1: Create Web Service

1. Go to your [Render Dashboard](https://dashboard.render.com/)
2. Click **"New"** → **"Web Service"**
3. Connect your GitHub repository: `https://github.com/gajjarkav/vishwakarmamechfab.git`

## ⚙️ Step 2: Configure Web Service

### Basic Configuration
- **Name**: `vishwakarmamechfab-web`
- **Environment**: `Python 3`
- **Region**: `Singapore` (same as your database for better performance)
- **Branch**: `main`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn vmf_project.wsgi:application`

### Advanced Settings
- **Auto-Deploy**: `Yes` (deploys automatically when you push to GitHub)

## 🔐 Step 3: Set Environment Variables

In the **Environment** section, add these variables:

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.6` |
| `DJANGO_SECRET_KEY` | Generate new key: Run `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DJANGO_DEBUG` | `False` |
| `DJANGO_ALLOWED_HOSTS` | `vishwakarmamechfab-web.onrender.com` (will be your app URL) |
| `DATABASE_URL` | `postgresql://kavygajjar:r0gYmyGlFRashWZ1lfznAo0CMFxdP1ZA@dpg-d4087tpr0fns73bhngfg-a.singapore-postgres.render.com/maindb_4rsy` |
| `DJANGO_SECURE_SSL_REDIRECT` | `True` |
| `DJANGO_SESSION_COOKIE_SECURE` | `True` |
| `DJANGO_CSRF_COOKIE_SECURE` | `True` |
| `DJANGO_SECURE_HSTS_SECONDS` | `31536000` |
| `DJANGO_ADMIN_URL` | `secure-admin-panel-xyz123/` |

## 📋 Step 4: Deploy

1. Click **"Create Web Service"**
2. Render will:
   - ✅ Clone your repository
   - ✅ Install dependencies from `requirements.txt`
   - ✅ Run `build.sh` (collect static files & migrate database)
   - ✅ Start your application with Gunicorn

## 🔧 Step 5: Post-Deployment Setup

### Create Superuser Account
1. Go to your web service dashboard
2. Click **"Shell"** tab
3. Run: `python manage.py createsuperuser`
4. Create your admin credentials

### Populate Database (Optional)
Run these commands in the Shell:
```bash
python manage.py populate_services
python manage.py populate_projects  
python manage.py populate_gallery
python manage.py populate_about
```

## 🌐 Step 6: Access Your Application

- **Website**: `https://vishwakarmamechfab-web.onrender.com`
- **Admin Panel**: `https://vishwakarmamechfab-web.onrender.com/secure-admin-panel-xyz123/`

## ⚡ Quick Deployment Checklist

- [ ] Web service created and connected to GitHub
- [ ] All environment variables set correctly
- [ ] DATABASE_URL points to your PostgreSQL database
- [ ] Build and deployment completed successfully
- [ ] Superuser account created
- [ ] Admin panel accessible
- [ ] Contact form working and submissions visible in admin

## 🔍 Troubleshooting

### If Build Fails:
- Check build logs for specific error messages
- Ensure `build.sh` is executable
- Verify all dependencies are in `requirements.txt`

### If App Won't Start:
- Check `DJANGO_ALLOWED_HOSTS` includes your Render URL
- Verify `DATABASE_URL` is correct
- Check application logs for Django errors

### If Database Connection Fails:
- Verify `DATABASE_URL` is exactly as provided by Render
- Ensure PostgreSQL database is in "available" status
- Check database connection logs

### If Static Files Don't Load:
- Verify `python manage.py collectstatic` runs in build
- Check WhiteNoise configuration in settings.py
- Ensure static file paths are correct

## 📊 Monitoring Your Application

### In Render Dashboard:
- **Metrics**: CPU, Memory, Response time
- **Logs**: Application and access logs
- **Events**: Deployment history
- **Shell**: Direct access to your application

### Database Monitoring:
- **Storage**: Monitor database size (1GB limit on free tier)
- **Connections**: Active database connections
- **Performance**: Query performance metrics

## 🎯 Next Steps After Deployment

1. **Custom Domain** (Optional): Add your own domain name
2. **Monitoring**: Set up alerts for downtime
3. **Backups**: Database is automatically backed up
4. **Scaling**: Consider paid plans for production traffic
5. **SSL**: Already configured and automatic

## 💡 Pro Tips

- **Free Tier Limitations**: Service sleeps after 15 minutes of inactivity
- **Startup Time**: First request after sleep takes ~30 seconds
- **Database**: 1GB storage limit on free PostgreSQL
- **Logs**: Keep checking logs during initial deployment
- **Environment**: Always use environment variables for secrets

Your Django application is now ready for production deployment on Render! 🚀