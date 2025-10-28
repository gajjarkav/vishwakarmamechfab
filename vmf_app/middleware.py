"""
Custom Security Middleware for VMF Project
Adds additional security headers and protections
"""

class SecurityHeadersMiddleware:
    """
    Middleware to add security headers to all responses
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Content Security Policy
        csp_directives = [
            "default-src 'self'",
            "script-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://kit.fontawesome.com https://ka-f.fontawesome.com",
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://ka-f.fontawesome.com",
            "font-src 'self' https://fonts.gstatic.com https://ka-f.fontawesome.com",
            "img-src 'self' data: https: http:",
            "connect-src 'self'",
            "frame-ancestors 'none'",
            "object-src 'none'",
            "base-uri 'self'",
            "form-action 'self'",
            "upgrade-insecure-requests"
        ]
        response['Content-Security-Policy'] = '; '.join(csp_directives)
        
        # Additional Security Headers
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=(), payment=(), usb=(), accelerometer=(), gyroscope=(), magnetometer=()'
        
        # Remove server information
        if 'Server' in response:
            del response['Server']
        
        # Cache control for sensitive pages
        if request.path.startswith('/admin'):
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        
        return response


class AdminSecurityMiddleware:
    """
    Additional security for admin pages
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Log admin access attempts (after authentication middleware has run)
        if (request.path.startswith('/admin') and 
            hasattr(request, 'user') and 
            not request.user.is_authenticated and
            response.status_code == 302):  # Redirect to login
            import logging
            logger = logging.getLogger('django.security')
            logger.warning(f'Unauthenticated admin access attempt from {self.get_client_ip(request)}')
        
        return response
    
    def get_client_ip(self, request):
        """Get client IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip