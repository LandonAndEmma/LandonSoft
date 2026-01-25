/**
 * Main Entry Point
 * Initializes the application and sets up routing
 */

import { Router } from './router.js';
import { setTitle, loadProjectList } from './utils.js';

// Export utilities to global scope for inline scripts
window.setTitle = setTitle;
window.loadProjectList = loadProjectList;

// Initialize router when DOM is loaded
const router = new Router();
router.init();
