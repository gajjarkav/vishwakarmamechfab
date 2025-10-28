/* =============== NAVIGATION MENU =============== */
const navMenu = document.getElementById('nav-menu');
const navToggle = document.getElementById('nav-toggle');
const navClose = document.getElementById('nav-close');
const navLinks = document.querySelectorAll('.nav__link');

// Show menu
if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.add('show-menu');
    });
}

// Hide menu
if (navClose) {
    navClose.addEventListener('click', () => {
        navMenu.classList.remove('show-menu');
    });
}

// Close menu when clicking on nav links
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('show-menu');
    });
});

/* =============== ACTIVE NAVIGATION LINK =============== */
const sections = document.querySelectorAll('section[id]');

const scrollActive = () => {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 100;
        const sectionId = current.getAttribute('id');
        const sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']');

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            sectionsClass.classList.add('active-link');
        } else {
            sectionsClass.classList.remove('active-link');
        }
    });
};

window.addEventListener('scroll', scrollActive);

/* =============== HEADER BACKGROUND ON SCROLL =============== */
const scrollHeader = () => {
    const header = document.getElementById('header');
    // Add a class if the bottom offset is greater than 50 of the viewport
    if (window.scrollY >= 50) {
        header.classList.add('scroll-header');
    } else {
        header.classList.remove('scroll-header');
    }
};

window.addEventListener('scroll', scrollHeader);

/* =============== SMOOTH SCROLLING =============== */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

/* =============== CONTACT FORM =============== */
const contactForm = document.getElementById('contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // Get form inputs and button
        const formInputs = this.querySelectorAll('.form__input');
        const submitButton = this.querySelector('.form__button');

        // Basic form validation
        let isValid = true;
        formInputs.forEach(input => {
            if (input.hasAttribute('required') && !input.value.trim()) {
                isValid = false;
                input.style.borderColor = '#ef4444';
                input.style.backgroundColor = 'rgba(239, 68, 68, 0.05)';
            } else {
                input.style.borderColor = 'var(--border-color)';
                input.style.backgroundColor = 'var(--container-color)';
            }
        });

        // Email validation
        const emailInput = this.querySelector('input[type="email"]');
        if (emailInput && emailInput.value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(emailInput.value)) {
                isValid = false;
                emailInput.style.borderColor = '#ef4444';
                emailInput.style.backgroundColor = 'rgba(239, 68, 68, 0.05)';
            }
        }

        if (!isValid) {
            showNotification('Please fill in all required fields correctly.', 'error');
            return;
        }

        // Prepare payload
        const payload = {
            name: this.querySelector('input#name') ? this.querySelector('input#name').value.trim() : '',
            email: this.querySelector('input#email') ? this.querySelector('input#email').value.trim() : '',
            subject: this.querySelector('input#subject') ? this.querySelector('input#subject').value.trim() : '',
            message: this.querySelector('textarea#message') ? this.querySelector('textarea#message').value.trim() : ''
        };

        // Show loading state
        submitButton.textContent = 'Sending...';
        submitButton.disabled = true;

        // Get CSRF token
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // Send to backend AJAX endpoint
        fetch('/contact/ajax/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(payload),
            credentials: 'same-origin'
        })
        .then(response => response.json())
        .then(data => {
            if (data && data.success) {
                contactForm.reset();
                showNotification(data.message || 'Message sent successfully!', 'success');
            } else {
                showNotification((data && data.message) || 'There was an error sending your message.', 'error');
            }
        })
        .catch(err => {
            console.error('Contact form submit error:', err);
            showNotification('There was a network error. Please try again later.', 'error');
        })
        .finally(() => {
            submitButton.textContent = 'Send Message';
            submitButton.disabled = false;
        });
    });
}

/* =============== NOTIFICATION SYSTEM =============== */
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.notification');
    existingNotifications.forEach(notification => notification.remove());
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.innerHTML = `
        <span class="notification__message">${message}</span>
        <button class="notification__close">&times;</button>
    `;
    
    // Add notification styles
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#10b981' : type === 'error' ? '#ef4444' : '#3b82f6'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        z-index: 1000;
        display: flex;
        align-items: center;
        gap: 1rem;
        font-weight: 500;
        transform: translateX(100%);
        transition: transform 0.3s ease;
    `;
    
    // Add to body
    document.body.appendChild(notification);
    
    // Show notification
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Close button functionality
    const closeButton = notification.querySelector('.notification__close');
    closeButton.style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0;
        margin-left: 0.5rem;
    `;
    
    closeButton.addEventListener('click', () => {
        hideNotification(notification);
    });
    
    // Auto hide after 5 seconds
    setTimeout(() => {
        if (document.body.contains(notification)) {
            hideNotification(notification);
        }
    }, 5000);
}

function hideNotification(notification) {
    notification.style.transform = 'translateX(100%)';
    setTimeout(() => {
        if (document.body.contains(notification)) {
            document.body.removeChild(notification);
        }
    }, 300);
}

/* =============== SCROLL ANIMATIONS =============== */
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

// Add animation classes to elements
document.addEventListener('DOMContentLoaded', () => {
    // Elements to animate
    const animateElements = document.querySelectorAll(
        '.service__card, .project__card, .client__card, .feature, .stat, .hero__content, .hero__logo-container'
    );
    
    animateElements.forEach((el, index) => {
        // Add initial animation styles
        el.style.cssText += `
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.45s ease-in, transform 0.45s ease-in;
            transition-delay: ${index * 0.02}s;
        `;
        
        // Observe for intersection
        observer.observe(el);
    });
});

// Add CSS for animation states
const animationStyles = document.createElement('style');
animationStyles.textContent = `
    .animate-in {
        opacity: 1 !important;
        transform: translateY(0) !important;
    }
    
    .scroll-header {
        background-color: rgba(255, 255, 255, 0.98) !important;
        box-shadow: 0 2px 12px rgba(15, 23, 42, 0.08) !important;
    }
`;
document.head.appendChild(animationStyles);

/* =============== PERFORMANCE OPTIMIZATIONS =============== */
// Debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debouncing to scroll events
const debouncedScrollActive = debounce(scrollActive, 10);
const debouncedScrollHeader = debounce(scrollHeader, 10);

window.removeEventListener('scroll', scrollActive);
window.removeEventListener('scroll', scrollHeader);
window.addEventListener('scroll', debouncedScrollActive);
window.addEventListener('scroll', debouncedScrollHeader);

/* =============== ACCESSIBILITY IMPROVEMENTS =============== */
// Keyboard navigation for mobile menu
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu.classList.contains('show-menu')) {
        navMenu.classList.remove('show-menu');
        navToggle.focus();
    }
});

// Focus management for mobile menu
navToggle.addEventListener('click', () => {
    setTimeout(() => {
        const firstNavLink = navMenu.querySelector('.nav__link');
        if (firstNavLink) {
            firstNavLink.focus();
        }
    }, 100);
});

/* =============== LAZY LOADING SIMULATION =============== */
// Simulate lazy loading for project images (in a real implementation, you'd use actual images)
const projectCards = document.querySelectorAll('.project__card');

const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const placeholder = entry.target.querySelector('.project__image-placeholder');
            if (placeholder) {
                placeholder.style.background = 'linear-gradient(135deg, #64748b, #94a3b8)';
                placeholder.style.transition = 'background 0.5s ease';
            }
            imageObserver.unobserve(entry.target);
        }
    });
});

projectCards.forEach(card => {
    imageObserver.observe(card);
});

/* =============== PROJECT MODAL =============== */
const modalOverlay = document.querySelector('.modal');
const modalClose = document.querySelector('.modal__close');

// Project data structure
const projectData = {
    'project-1': {
        title: 'Industrial HVAC System Design',
        category: 'Manufacturing',
        description: 'Comprehensive design and implementation of a state-of-the-art HVAC system for a 50,000 sq ft manufacturing facility. The project involved custom ductwork fabrication, energy-efficient unit installation, and automated climate control systems integration.',
        image: 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
        client: 'Industrial Solutions Ltd',
        date: 'January 2024'
    },
    'project-2': {
        title: 'Automated Assembly Line',
        category: 'Automation',
        description: 'Design and implementation of a fully automated assembly line system that increased production efficiency by 30%. The project included custom machinery fabrication, robotic integration, and advanced control systems.',
        image: 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
        client: 'AutoTech Industries',
        date: 'March 2024'
    },
    'project-3': {
        title: 'Power Plant Equipment Maintenance',
        category: 'Energy',
        description: 'Comprehensive maintenance and optimization program for critical power generation equipment. The project involved preventive maintenance protocols, equipment upgrades, and efficiency improvements.',
        image: 'https://res.cloudinary.com/dxtx1kkwy/image/upload/v1737025117/WhatsApp_Image_2025-01-16_at_10.03.48_01ed99bf_glcnhc.jpg',
        client: 'Energy Systems Corp',
        date: 'May 2024'
    }
};

// Open modal function
function openModal(projectId) {
    const project = projectData[projectId];
    if (!project) {
        console.error('No project found with ID:', projectId);
        return;
    }

    // Update modal content
    const modalTitle = document.querySelector('#modalTitle');
    const modalCategory = document.querySelector('#modalCategory');
    const modalDescription = document.querySelector('#modalDescription');
    const modalImage = document.querySelector('.modal__image img');

    if (modalTitle) modalTitle.textContent = project.title;
    if (modalCategory) modalCategory.textContent = project.category;
    if (modalDescription) modalDescription.textContent = project.description;
    
    if (modalImage) {
        modalImage.src = project.image;
        modalImage.alt = project.title;
    }
    
    // Update specifications
    const clientSpec = document.querySelector('[data-spec="client"] .modal__spec-value');
    const dateSpec = document.querySelector('[data-spec="date"] .modal__spec-value');
    
    if (clientSpec) clientSpec.textContent = project.client;
    if (dateSpec) dateSpec.textContent = project.date;

    // Show modal with fade effect
    if (modalOverlay) {
        modalOverlay.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        // Add animation class after a small delay to ensure the transition works
        setTimeout(() => {
            modalOverlay.classList.add('modal--active');
        }, 10);
    }
}

// Close modal function
function closeModal() {
    modalOverlay.classList.remove('modal--active');
    
    // Wait for animation to complete before hiding
    setTimeout(() => {
        modalOverlay.style.display = 'none';
        document.body.style.overflow = '';
    }, 300);
}

// Add click events to project cards
document.addEventListener('DOMContentLoaded', () => {
    // Add click events to Read More buttons
    const readMoreButtons = document.querySelectorAll('.project__btn');
    readMoreButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const projectCard = button.closest('.project__card');
            if (projectCard) {
                const projectId = projectCard.getAttribute('data-project');
                openModal(projectId);
            }
        });
    });

    // Close modal events
    if (modalClose) {
        modalClose.addEventListener('click', (e) => {
            e.preventDefault();
            closeModal();
        });
    }

    // Close on overlay click
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) {
            closeModal();
        }
    });

    // Close on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modalOverlay.style.display === 'block') {
            closeModal();
        }
    });
});

/* =============== THEME MANAGEMENT =============== */
// Future enhancement: Add theme switching capability
function initializeTheme() {
    // Check for saved theme preference or default to 'light'
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
}

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', initializeTheme);

/* =============== SCROLL TO TOP =============== */
const scrollToTopBtn = document.getElementById('scrollToTop');
let scrollTimeout;

// Show/hide button based on scroll position
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        scrollToTopBtn.classList.add('show');
        
        // Clear the existing timeout
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        
        // Set new timeout to hide the button after 3 seconds
        scrollTimeout = setTimeout(() => {
            scrollToTopBtn.classList.remove('show');
        }, 3000);
    } else {
        scrollToTopBtn.classList.remove('show');
    }
});

// Scroll to top when button is clicked
scrollToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

/* =============== VIDEO PLAYER CONTROLS =============== */
document.addEventListener('DOMContentLoaded', function() {
    const video = document.querySelector('.video-player__video');
    const playPauseBtn = document.querySelector('.video-player__play-pause');
    const muteBtn = document.querySelector('.video-player__mute');
    const progressBar = document.querySelector('.video-player__progress-bar');
    const playIcon = document.querySelector('.video-player__play-icon');
    const pauseIcon = document.querySelector('.video-player__pause-icon');
    const volumeIcon = document.querySelector('.video-player__volume-icon');
    const muteIcon = document.querySelector('.video-player__mute-icon');

    if (!video) return; // Exit if video element not found

    // Initialize video state
    let isPlaying = true; // Video starts with autoplay
    let isMuted = true;   // Video starts muted

    // Update UI to match initial state
    updatePlayPauseIcon();
    updateMuteIcon();

    // Play/Pause functionality
    if (playPauseBtn) {
        playPauseBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            togglePlayPause();
        });
    }

    // Mute/Unmute functionality
    if (muteBtn) {
        muteBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            toggleMute();
        });
    }

    // Video click to play/pause (but not when clicking controls)
    video.addEventListener('click', (e) => {
        // Don't toggle if clicking on control buttons
        if (e.target.closest('.video-control-btn')) {
            return;
        }
        e.preventDefault();
        togglePlayPause();
    });

    // Update progress bar
    video.addEventListener('timeupdate', updateProgress);

    // Video ended
    video.addEventListener('ended', () => {
        // Video has loop attribute, so this shouldn't trigger often
        isPlaying = false;
        updatePlayPauseIcon();
    });

    // Video play/pause events (for external controls like browser)
    video.addEventListener('play', () => {
        isPlaying = true;
        updatePlayPauseIcon();
    });

    video.addEventListener('pause', () => {
        isPlaying = false;
        updatePlayPauseIcon();
    });

    // Functions
    function togglePlayPause() {
        if (isPlaying) {
            video.pause();
            isPlaying = false;
        } else {
            video.play().catch(e => console.log('Video play failed:', e));
            isPlaying = true;
        }
        updatePlayPauseIcon();
    }

    function toggleMute() {
        if (isMuted) {
            video.muted = false;
            isMuted = false;
        } else {
            video.muted = true;
            isMuted = true;
        }
        updateMuteIcon();
    }

    function updatePlayPauseIcon() {
        if (playIcon && pauseIcon) {
            if (isPlaying) {
                playIcon.style.display = 'none';
                pauseIcon.style.display = 'block';
            } else {
                playIcon.style.display = 'block';
                pauseIcon.style.display = 'none';
            }
        }
    }

    function updateMuteIcon() {
        if (volumeIcon && muteIcon) {
            if (isMuted) {
                volumeIcon.style.display = 'none';
                muteIcon.style.display = 'block';
            } else {
                volumeIcon.style.display = 'block';
                muteIcon.style.display = 'none';
            }
        }
    }

    function updateProgress() {
        if (progressBar && video.duration) {
            const progress = (video.currentTime / video.duration) * 100;
            progressBar.style.width = progress + '%';
        }
    }

    // Handle video load errors gracefully
    video.addEventListener('error', (e) => {
        console.log('Video load error:', e);
        // You can add fallback behavior here
    });

    // Intersection Observer for performance
    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Video is visible, ensure it's playing if it should be
                if (isPlaying && video.paused) {
                    video.play().catch(e => console.log('Auto-play failed:', e));
                }
            } else {
                // Video is not visible, pause it for performance
                if (isPlaying && !video.paused) {
                    video.pause();
                }
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of video is visible
    });

    videoObserver.observe(video);
});

console.log('Vishwakarma Mechfab website loaded successfully!');