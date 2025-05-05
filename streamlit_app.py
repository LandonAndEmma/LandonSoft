# app.py
import streamlit as st
import json
import base64
from pathlib import Path

# Configuration
st.set_page_config(
    page_title="LandonSoft",
    page_icon=":video_game:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load data
with open(Path("assets/data/project-list.json"), "r") as f:
    projects = json.load(f)

# Custom CSS
def inject_css():
    st.markdown(f"""
    <style>
    {Path("assets/css/style.regular.css").read_text()}
    .stApp {{
        background-color: var(--main-background);
    }}
    .stMarkdown {{
        max-width: 100%;
    }}
    iframe {{
        padding: 1rem;
    }}
    html, body, #root, .stApp {{
      width: 100%;
      height: 100%;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }}
    [data-testid="stAppViewContainer"] > .main > .block-container {{
      padding: 0 !important;
      max-width: 100% !important;
      width: 100% !important;
    }}
    #top-bar {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      z-index: 1000;           /* sit above everything */
      background-color: var(--main-gray);
    }}
    .main {{
      padding-top: 4.5rem;     /* adjust this to match your #top-bar height */
    }}
    #footer {{
      position: relative;
      width: 100vw;
      left: 0;
      padding-bottom: 1rem;
    }}
    </style>
    """, unsafe_allow_html=True)

def svg_icon(path):
    return f"data:image/svg+xml;base64,{base64.b64encode(Path(path).read_bytes()).decode()}"
# Header
def render_header():
    current_page = st.query_params.get("page", "")
    st.markdown(f"""
    <div id="top-bar">
        <div id="top-bar-title">
            <a href="#/">
                <img class="logo" src="{svg_icon('assets/svg/logo_notext.svg')}" />
                <img class="logo-sm" src="{svg_icon('assets/svg/logo.svg')}" />
            </a>
            <h1 class="logo-title">LandonSoft</h1>
        </div>
        <ul id="top-bar-menu">
            <li><a href="?page=home" class="{'active' if current_page in ['home', ''] else ''}">Home</a></li>
            <li><a href="?page=projects" class="{'active' if current_page == 'projects' else ''}">Projects</a></li>
            <li><a href="?page=youtube" class="{'active' if current_page == 'youtube' else ''}">YouTube</a></li>
            <li><a href="?page=about" class="{'active' if current_page == 'about' else ''}">About Me</a></li>
            <li><a href="?page=contact" class="{'active' if current_page == 'contact' else ''}">Contact</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# Footer
def render_footer():
    st.markdown(f"""
    <footer id="footer">
        <p><span>&copy; 2024 Landon & Emma</span></p>
        <p>
            <a class="mx-1" href="https://www.youtube.com/@LandonEmma">
                <img class="svg-icon" src="{svg_icon('assets/svg/youtube.svg')}" />
            </a>
            <a class="mx-1" href="https://discord.gg/PjbUeqAKTn">
                <img class="svg-icon" src="{svg_icon('assets/svg/discord.svg')}" />
            </a>
            <a class="mx-1" href="https://github.com/LandonAndEmma">
                <img class="svg-icon" src="{svg_icon('assets/svg/github.svg')}" />
            </a>
        </p>
    </footer>
    """, unsafe_allow_html=True)


# Project template
def project_entry(project, full=False):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(project['icon'], width=64)
    with col2:
        st.markdown(f"""
        <h3><a href="{project['url']}">{project['name']}</a></h3>
        <p>{project['description']}</p>
        <div class="project-footer">
            <div class="project-tags">
                {"".join([f'<span class="pill">{tag}</span>' for tag in project["tags"]])}
            </div>
            <div class="project-links">
                {"".join([f'<a href="{link["url"]}"><img class="svg-icon" src="{svg_icon(link["icon"])}"></a>'
                          for link in project["links"]])}
            </div>
        </div>
        """, unsafe_allow_html=True)


# Pages
def home():
    with st.container():
        st.markdown("""
        <div class="container">
            <div class="content-left">
                <h1>Welcome</h1>
                <p>I'm Landon Perkins, homebrew, tools and game developer.</p>
                <p>You probably know me for my remixes of Nintendo music and for the unreleased MySims Kart DS.</p>
                <p>If you want to talk go to the <a href="?page=contact">contacts</a> page.</p>
            </div>
            <div class="content-right">
                <h1>Most notable projects</h1>
        """, unsafe_allow_html=True)

        for project in projects[:3]:
            project_entry(project)

        st.markdown("""
                <div style="text-align: center; margin-top: 1em;">
                    <a href="?page=projects">See more...</a>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def projects_page():
    with st.container():
        st.markdown("""
        <div class="container">
            <div class="content-center">
                <h1>My Projects</h1>
        """, unsafe_allow_html=True)

        for project in projects:
            project_entry(project, full=True)

        st.markdown("</div></div>", unsafe_allow_html=True)


def about():
    with st.container():
        st.markdown("""
        <div class="container">
            <div class="content-left">
                <h1>About Me</h1>
                <p>I'm Landon Perkins, a Christian, modder, remixer, and game developer born on 11/10/2006</p>
                <p>You probably know me for my remixes of Nintendo music and Mario Kart DS ROM hacks.</p>
                <p>Loves: God, Jesus, The Bible, Mario Kart, Nintendo, music, Mario, Fortnite, Minecraft, playing outside, coding, 2000s - 2010s nostalgia, my friends.</p>
                <p>Stuff I own: Wii (Bought on 2008 or 2011, Sold in 2014 but bought a new one in 2021), 3DS (2013), Wii U (2013 or 2014), HP Gaming Pavilion - 15-ec1073d (Fall of 2019) Switch (Bought on release week, sold on OLED release day and bought that one)</p>
                <p>If you want to talk go to the <a href="?page=contact">contacts</a> page.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


def contact():
    with st.container():
        st.markdown(f"""
        <div class="container">
            <div class="content-center">
                <h1>Contact</h1>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2em;">
                    <div>
                        <h2>YouTube</h2>
                        <a class="contact-entry" href="https://www.youtube.com/@LandonEmma">
                            <img class="svg-icon" src="{svg_icon('assets/svg/youtube.svg')}" />
                            <span>YouTube Channel</span>
                        </a>
                    </div>
                    <div>
                        <h2>Discord</h2>
                        <a class="contact-entry" href="https://discord.gg/PjbUeqAKTn">
                            <img class="svg-icon" src="{svg_icon('assets/svg/discord.svg')}" />
                            <span>Discord Server</span>
                        </a>
                    </div>
                    <div>
                        <h2>GitHub</h2>
                        <a class="contact-entry" href="https://github.com/LandonAndEmma">
                            <img class="svg-icon" src="{svg_icon('assets/svg/github.svg')}" />
                            <span>GitHub Profile</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def youtube():
    with st.container():
        st.markdown("""
        <div class="container">
            <div class="content-center">
                <h1>Newest Videos</h1>
                <div class="videos">
                    <iframe src="https://www.youtube.com/embed?listType=playlist&list=UULFYYDcTwZ9cf9YLw0qbqEBLQ&index=1" 
                            class="latestVideoEmbed" vnum='1' frameborder="0" allowfullscreen></iframe>
                    <iframe src="https://www.youtube.com/embed?listType=playlist&list=UULFYYDcTwZ9cf9YLw0qbqEBLQ&index=2" 
                            class="latestVideoEmbed" vnum='2' frameborder="0" allowfullscreen></iframe>
                    <iframe src="https://www.youtube.com/embed?listType=playlist&list=UULFYYDcTwZ9cf9YLw0qbqEBLQ&index=3" 
                            class="latestVideoEmbed" vnum='3' frameborder="0" allowfullscreen></iframe>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# Main app
def main():
    inject_css()
    render_header()

    page = st.query_params.get("page", "home")

    pages = {
        "home": home,
        "projects": projects_page,
        "youtube": youtube,
        "about": about,
        "contact": contact
    }

    if page in pages:
        pages[page]()
    else:
        st.error("Page not found")

    render_footer()


if __name__ == "__main__":
    main()