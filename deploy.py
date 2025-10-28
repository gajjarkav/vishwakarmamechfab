#!/usr/bin/env python
"""
Production deployment script for VMF Project
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout.strip():
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(e.stderr)
        return False

def main():
    print("🚀 Starting VMF Project Deployment")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Run deployment steps
    steps = [
        ("python manage.py migrate", "Running database migrations"),
        ("python manage.py collectstatic --noinput", "Collecting static files"),
    ]
    
    success = True
    for command, description in steps:
        if not run_command(command, description):
            success = False
            break
    
    if success:
        print("\n🎉 Deployment completed successfully!")
        print("\nNext steps:")
        print("1. Create a superuser: python manage.py createsuperuser")
        print("2. Start the server: python manage.py runserver")
        print("3. Or use Gunicorn: gunicorn vmf_project.wsgi:application")
    else:
        print("\n💥 Deployment failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()