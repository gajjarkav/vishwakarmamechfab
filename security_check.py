#!/usr/bin/env python
"""
Security Check Script for VMF Project
Tests security headers and configurations
"""

import os
import sys
import django
import requests
from urllib.parse import urljoin

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vmf_project.settings')
django.setup()

from django.conf import settings
from django.test import Client
from django.urls import reverse

class SecurityChecker:
    def __init__(self, base_url='http://127.0.0.1:8000'):
        self.base_url = base_url
        self.client = Client()
        
    def check_security_headers(self):
        """Check if security headers are properly set"""
        print("🔒 Checking Security Headers...")
        print("=" * 50)
        
        # Test main page
        response = self.client.get('/')
        headers = response.headers if hasattr(response, 'headers') else response
        
        security_headers = {
            'Content-Security-Policy': 'CSP header for XSS protection',
            'X-Content-Type-Options': 'Prevents MIME type sniffing',
            'X-Frame-Options': 'Clickjacking protection',
            'X-XSS-Protection': 'XSS filter',
            'Referrer-Policy': 'Controls referrer information',
            'Strict-Transport-Security': 'HSTS for HTTPS enforcement',
        }
        
        for header, description in security_headers.items():
            if header in headers:
                print(f"✅ {header}: {headers[header]}")
            else:
                print(f"❌ {header}: Missing - {description}")
        
        print()
    
    def check_admin_security(self):
        """Check admin panel security"""
        print("🛡️ Checking Admin Security...")
        print("=" * 50)
        
        # Test admin access without authentication
        response = self.client.get('/admin/')
        if response.status_code == 302:  # Redirect to login
            print("✅ Admin panel requires authentication")
        else:
            print("❌ Admin panel is accessible without authentication")
        
        # Check admin cache headers
        if 'Cache-Control' in response:
            print(f"✅ Admin Cache Control: {response['Cache-Control']}")
        else:
            print("❌ Admin cache control headers missing")
        
        print()
    
    def check_csrf_protection(self):
        """Check CSRF protection"""
        print("🛡️ Checking CSRF Protection...")
        print("=" * 50)
        
        # Test contact form without CSRF token
        response = self.client.post('/contact/ajax/', 
                                  data='{"name": "test"}', 
                                  content_type='application/json')
        
        if response.status_code == 403:
            print("✅ CSRF protection is active")
        else:
            print("❌ CSRF protection may be disabled")
        
        print()
    
    def check_cookie_security(self):
        """Check cookie security settings"""
        print("🍪 Checking Cookie Security...")
        print("=" * 50)
        
        # Check session cookie settings
        print(f"Session Cookie Secure: {settings.SESSION_COOKIE_SECURE}")
        print(f"Session Cookie HttpOnly: {settings.SESSION_COOKIE_HTTPONLY}")
        print(f"Session Cookie SameSite: {settings.SESSION_COOKIE_SAMESITE}")
        print(f"CSRF Cookie Secure: {settings.CSRF_COOKIE_SECURE}")
        print(f"CSRF Cookie HttpOnly: {settings.CSRF_COOKIE_HTTPONLY}")
        
        print()
    
    def check_debug_mode(self):
        """Check if debug mode is disabled"""
        print("🐛 Checking Debug Mode...")
        print("=" * 50)
        
        if settings.DEBUG:
            print("❌ DEBUG is True - Should be False in production")
        else:
            print("✅ DEBUG is False - Good for production")
        
        print()
    
    def check_allowed_hosts(self):
        """Check allowed hosts configuration"""
        print("🌐 Checking Allowed Hosts...")
        print("=" * 50)
        
        print(f"Allowed Hosts: {settings.ALLOWED_HOSTS}")
        
        if '*' in settings.ALLOWED_HOSTS:
            print("❌ Wildcard in ALLOWED_HOSTS - Security risk")
        elif settings.ALLOWED_HOSTS:
            print("✅ ALLOWED_HOSTS is properly configured")
        else:
            print("❌ ALLOWED_HOSTS is empty")
        
        print()
    
    def check_secret_key(self):
        """Check secret key security"""
        print("🔑 Checking Secret Key...")
        print("=" * 50)
        
        if settings.SECRET_KEY == 'django-insecure-a*7y-x5+$v$ckcnu$aje!$mqgc&@zdr@!(csd_@(e-(6u2&ypc':
            print("❌ Using default secret key - Generate a new one!")
        elif 'django-insecure' in settings.SECRET_KEY:
            print("❌ Using Django insecure secret key")
        elif len(settings.SECRET_KEY) < 50:
            print("❌ Secret key too short")
        else:
            print("✅ Secret key appears secure")
        
        print()
    
    def generate_security_report(self):
        """Generate comprehensive security report"""
        print("🔍 VMF Project Security Assessment")
        print("=" * 50)
        print()
        
        self.check_debug_mode()
        self.check_secret_key()
        self.check_allowed_hosts()
        self.check_security_headers()
        self.check_admin_security()
        self.check_csrf_protection()
        self.check_cookie_security()
        
        print("📋 Security Recommendations:")
        print("=" * 50)
        print("1. Ensure HTTPS is enabled in production")
        print("2. Use environment variables for sensitive settings")
        print("3. Regular security updates for Django and dependencies")
        print("4. Implement rate limiting for admin and contact forms")
        print("5. Regular security audits and penetration testing")
        print("6. Monitor security logs for suspicious activity")
        print("7. Use strong passwords for admin accounts")
        print("8. Consider using Django security middleware")
        print("9. Implement proper backup and recovery procedures")
        print("10. Use HTTPS-only cookies in production")

def main():
    """Run security checks"""
    checker = SecurityChecker()
    checker.generate_security_report()

if __name__ == "__main__":
    main()