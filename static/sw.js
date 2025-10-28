// Simple Service Worker for Vishwakarma Mechfab
// This prevents 404 errors for /sw.js requests

self.addEventListener('install', function(event) {
    console.log('Service Worker: Installing...');
    self.skipWaiting();
});

self.addEventListener('activate', function(event) {
    console.log('Service Worker: Activating...');
    event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', function(event) {
    // Let the browser handle all fetch requests normally
    // This is a minimal service worker just to prevent 404 errors
    return;
});