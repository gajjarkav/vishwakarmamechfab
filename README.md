# Vishwakarma Mechfab - Django Website

This is the Django-based website for Vishwakarma Mechfab, a mechanical engineering and fabrication company.

## Project Structure

```
vmf/                          # Main project directory
├── vmf_project/             # Django project root
│   ├── manage.py           # Django management script
│   ├── db.sqlite3          # SQLite database
│   ├── templates/          # HTML templates
│   │   ├── index.html     # Homepage
│   │   ├── gallery.html   # Gallery page
│   │   └── projects.html  # Projects page
│   ├── static/            # Static files (CSS, JS, Images)
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   ├── vmf_project/       # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── vmf_app/           # Django app
│       ├── views.py
│       ├── urls.py
│       ├── models.py
│       ├── admin.py
│       └── migrations/
└── .venv/                 # Virtual environment (Python)
```

## Setup Instructions

### 1. Activate Virtual Environment

```powershell
# Navigate to project directory
cd "c:\Users\mkgaj\OneDrive\Desktop\vmf\vmf_project"

# Activate virtual environment
..\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies (if needed)

```powershell
pip install django
```

### 3. Run Database Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)

```powershell
python manage.py createsuperuser
```

### 5. Run Development Server

```powershell
python manage.py runserver
```

The website will be available at: `http://127.0.0.1:8000/`

## URL Routes

- **Homepage**: `http://127.0.0.1:8000/`
- **Gallery**: `http://127.0.0.1:8000/gallery/`
- **Projects**: `http://127.0.0.1:8000/projects/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

## Features

- Responsive design for all devices
- Modern UI with smooth animations
- SEO optimized with meta tags and structured data
- Multiple pages: Home, Gallery, Projects
- Contact form integration ready
- Client showcase section
- Services and about sections

## Technologies Used

- **Backend**: Django 5.2.7
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite3
- **Fonts**: Google Fonts (Inter)
- **Images**: Cloudinary CDN

## Development Notes

- Static files are configured in `vmf_project/settings.py`
- Templates use Django template tags (`{% load static %}`, `{% url %}`)
- CSRF protection is enabled for forms
- Debug mode is ON (remember to turn OFF in production)

## Admin Documentation

For website administrators and content managers:
- **Complete Admin Guide**: See `ADMIN_README.md`
- **Quick Reference**: See `ADMIN_QUICK_REFERENCE.md`
- **Admin Panel URL**: https://vishwakarmamechfab.in/admin

## Deployment

For deployment instructions, see `DEPLOYMENT.md`

## Contact

Developed by Kavy Gajjar & Bhavansi Jethva

For more information, visit: [vishwakarmamechfab.in](https://vishwakarmamechfab.in)
