/**
 * Router Module
 * Handles client-side routing and page navigation
 */

import { setTitle, setInnerHTML } from './utils.js';

export class Router {
    constructor() {
        this.routes = new Map();
        this.templates = new Map();
        this.mainContent = document.getElementById('main-content');
        this.loadingElement = this.mainContent.querySelector('.loading');
        this.setupRoutes();
    }

    /**
     * Define a route
     */
    route(path, handler) {
        if (typeof handler === 'function') {
            this.routes.set(path, handler);
        } else if (typeof handler === 'string' && this.templates.has(handler)) {
            this.routes.set(path, this.templates.get(handler));
        }
        return this;
    }

    /**
     * Define a template
     */
    template(name, handler) {
        this.templates.set(name, handler);
        return this;
    }

    /**
     * Load and display a view
     */
    async view(url, title) {
        try {
            this.showLoading();
            
            const response = await fetch(url);
            
            if (!response.ok) {
                throw new Error(`Failed to load page: ${response.status}`);
            }
            
            const html = await response.text();
            
            setInnerHTML(this.mainContent, html);
            setTitle(title);
            
            this.hideLoading();
        } catch (error) {
            console.error('Error loading view:', error);
            this.showError(error.message);
        }
    }

    /**
     * Show loading state
     */
    showLoading() {
        if (this.loadingElement) {
            this.loadingElement.classList.remove('hidden');
            this.loadingElement.setAttribute('aria-busy', 'true');
        }
    }

    /**
     * Hide loading state
     */
    hideLoading() {
        if (this.loadingElement) {
            this.loadingElement.classList.add('hidden');
            this.loadingElement.setAttribute('aria-busy', 'false');
        }
    }

    /**
     * Show error message
     */
    showError(message) {
        const errorHTML = `
            <div class="container single-column">
                <div class="content-center">
                    <h1>Oops! Something went wrong</h1>
                    <p>${message}</p>
                    <p><a href="#/">Return to home</a></p>
                </div>
            </div>
        `;
        setInnerHTML(this.mainContent, errorHTML);
        setTitle('Error');
        this.hideLoading();
    }

    /**
     * Resolve and execute a route
     */
    async resolveRoute(path) {
        const handler = this.routes.get(path);
        
        if (handler) {
            await handler();
        } else {
            // 404 - Route not found
            this.show404();
        }
    }

    /**
     * Show 404 page
     */
    show404() {
        const notFoundHTML = `
            <div class="container single-column">
                <div class="content-center">
                    <h1>404 - Page Not Found</h1>
                    <p>The page you're looking for doesn't exist.</p>
                    <p><a href="#/">Return to home</a></p>
                </div>
            </div>
        `;
        setInnerHTML(this.mainContent, notFoundHTML);
        setTitle('Page Not Found');
        this.hideLoading();
    }

    /**
     * Handle route changes
     */
    async handleRoute() {
        const hash = window.location.hash.slice(1) || '/';
        console.log('Navigating to:', hash);
        await this.resolveRoute(hash);
    }

    /**
     * Setup all routes and templates
     */
    setupRoutes() {
        // Define page templates
        this.template('home', () => this.view('pages/home.html'));
        this.template('projects', () => this.view('pages/projects.html', 'Projects'));
        this.template('youtube', () => this.view('pages/youtube.html', 'Videos'));
        this.template('about', () => this.view('pages/about.html', 'About Me'));
        this.template('socialmedia', () => this.view('pages/socialmedia.html', 'Social Media'));
        
        // Project pages
        this.template('projects-neko-chronicles', () => this.view('pages/projects/neko-chronicles.html', 'Neko Chronicles'));
        this.template('projects-arm9-editor', () => this.view('pages/projects/arm9-editor.html', 'MKDS ARM9 Editor'));
        this.template('projects-disgaea-ds-manager', () => this.view('pages/projects/disgaea-ds-manager.html', 'Disgaea DS Manager'));
        this.template('projects-mysims-kart-ds', () => this.view('pages/projects/mysims-kart-ds.html', 'MySims Kart DS'));
        
        // Define routes
        this.route('/', 'home');
        this.route('/projects', 'projects');
        this.route('/youtube', 'youtube');
        this.route('/about', 'about');
        this.route('/socialmedia', 'socialmedia');
        this.route('/projects/neko-chronicles', 'projects-neko-chronicles');
        this.route('/projects/arm9-editor', 'projects-arm9-editor');
        this.route('/projects/disgaea-ds-manager', 'projects-disgaea-ds-manager');
        this.route('/projects/mysims-kart-ds', 'projects-mysims-kart-ds');
    }

    /**
     * Initialize the router
     */
    init() {
        // Handle route changes
        window.addEventListener('hashchange', () => this.handleRoute());
        window.addEventListener('load', () => this.handleRoute());
        
        console.log('Router initialized');
    }
}
