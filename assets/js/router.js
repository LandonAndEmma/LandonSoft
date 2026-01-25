let routes = {};
let templates = {};
function view(url, title) {
    let appDiv = document.getElementById("main-content");
    fetch(url).then(function (page) {
        return page.text();
    }).then(function (html) {
        setInnerHTML(appDiv, html);
        setTitle(title);
    });
}
function route(path, template) {
    if (typeof template === 'function') {
        return routes[path] = template;
    }
    else if (typeof template === 'string') {
        return routes[path] = templates[template];
    } else {
        return;
    };
};
function template(name, templateFunction) {
    return templates[name] = templateFunction;
};
function resolveRoute(route) {
    try {
        return routes[route];
    } catch (e) {
        throw new Error(`Route ${route} not found`);
    };
};
function router(evt) {
    let url = window.location.hash.slice(1) || '/';
    let routeFunc = resolveRoute(url);
    console.log(url);
    routeFunc();
};
function initRoutes() {
    // Define templates here
    template('home', () => view("pages/home.htm"));
    template('projects', () => view("pages/projects.htm", "Projects"));
    template('youtube', () => view("pages/youtube.htm", "Videos"));
    template('about', () => view("pages/about.htm", "About Me"));
    template('socialmedia', () => view("pages/socialmedia.htm", "Social Media"));
    template('projects-neko-chronicles', () => view("pages/projects/neko-chronicles.htm", "Neko Chronicles"));
    template('projects-arm9-editor', () => view("pages/projects/arm9-editor.htm", "MKDS ARM9 Editor"));
	template('projects-disgaea-ds-manager', () => view("pages/projects/disgaea-ds-manager.htm", "Disgaea DS Manager"));
	template('projects-mysims-kart-ds', () => view("pages/projects/mysims-kart-ds.htm", "MySims Kart DS"));
    // Define routes here
    route('/', 'home');
    route('/projects', 'projects');
    route('/youtube', 'youtube');
    route('/about', 'about');
    route('/socialmedia', 'socialmedia');
    route('/projects/neko-chronicles', 'projects-neko-chronicles');
    route('/projects/arm9-editor', 'projects-arm9-editor');
	route('/projects/disgaea-ds-manager', 'projects-disgaea-ds-manager');
	route('/projects/mysims-kart-ds', 'projects-mysims-kart-ds');
}
initRoutes();
// Add event listeners
window.addEventListener('load', router);
window.addEventListener('hashchange', router);