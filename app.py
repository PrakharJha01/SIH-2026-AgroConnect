"""
AgroConnect - Smart Market Linkages Platform for Farmers
Main Streamlit Application Entry Point
"""
import streamlit as st
from utils.session import init_session_state, is_logged_in, get_user_role
from utils.constants import ROLE_FARMER, ROLE_BUYER

# Page configuration
st.set_page_config(
    page_title="AgroConnect - Market Linkages Platform",
    page_icon="logo.jpeg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Set the Sidebar Logo spanning across all pages
st.logo("logo.jpeg", icon_image="logo.jpeg")

# Initialize session state
init_session_state()

# Custom CSS
st.markdown("""
<style>
    /* AgroConnect Modern Design System */
    :root {
        --primary-green: #16a34a;
        --dark-green: #15803d;
        --light-green: #dcfce7;
        --accent-orange: #f59e0b;
        --text-dark: #0f172a;
        --text-muted: #64748b;
        --bg-main: #f8fafc;
        --bg-card: #ffffff;
    }

    /* Modern Typography */
    h1, h2, h3, h4 {
        color: var(--text-dark) !important;
        font-family: "Inter", "Segoe UI", sans-serif !important;
        letter-spacing: -0.02em;
    }

    hr {
        margin: 1.5rem 0 !important;
        border-color: #e2e8f0 !important; 
    }

    /* Streamlit Primary Button Overrides */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--primary-green) 0%, var(--dark-green) 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.6rem 2rem !important;
        border: none !important;
        box-shadow: 0 4px 6px -1px rgba(22, 163, 74, 0.2), 0 2px 4px -2px rgba(22, 163, 74, 0.2) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 15px -3px rgba(22, 163, 74, 0.3) !important;
    }

    /* Streamlit Secondary Button Overrides */
    .stButton > button[kind="secondary"] {
        background-color: white !important;
        color: var(--text-dark) !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    .stButton > button[kind="secondary"]:hover {
        border-color: var(--primary-green) !important;
        color: var(--primary-green) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05) !important;
    }

    /* Dashboard Re-usable component rules (Stat Cards) */
    .stat-card {
        background: var(--bg-card);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);
        text-align: center;
        border-bottom: 4px solid var(--primary-green);
        transition: transform 0.2s ease-in-out;
    }
    .stat-card:hover {
        transform: translateY(-3px);
    }
    .stat-number {
        font-size: 2.2rem;
        font-weight: 800;
        color: var(--primary-green);
        margin: 0;
        line-height: 1.2;
    }
    .stat-label {
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-muted);
        text-transform: uppercase;
        margin-top: 0.5rem;
        letter-spacing: 0.5px;
    }

    /* Custom classes used in older components (kept for fallback compatibility) */
    .main-header {
        background: linear-gradient(135deg, var(--primary-green) 0%, var(--dark-green) 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(22, 163, 74, 0.2);
    }
    .feature-card {
        background: var(--bg-card);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid var(--primary-green);
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    .feature-card:hover { transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
    
    .info-box {
        background: #f0f9ff;
        border-left: 4px solid #0ea5e9;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: #0369a1;
        font-weight: 500;
    }

    /* Action Cards for Dashboards */
    .action-card {
        background: var(--bg-card);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
        border: 1px solid #e2e8f0;
        border-left: 4px solid var(--primary-green);
        transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .action-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        border-color: #cbd5e1;
    }
    .action-card h3 {
        margin-top: 0;
        margin-bottom: 0.5rem;
        font-size: 1.1rem !important;
    }
    .action-card p {
        color: var(--text-muted);
        margin: 0;
        font-size: 0.95rem;
    }

    /* Native metrics styling tweaks */
    [data-testid="stMetricValue"] {
        font-weight: 800 !important;
        color: var(--primary-green) !important;
    }
    [data-testid="stMetricLabel"] {
        font-weight: 600 !important;
        color: var(--text-muted) !important;
    }

    /* Tabs tweaks */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 55px;
        border-radius: 8px 8px 0 0 !important;
        color: var(--text-muted);
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        color: var(--primary-green) !important;
        border-bottom-color: var(--primary-green) !important;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Navigation: role-based page sections
# ---------------------------------------------------------------------------

# Shared pages (visible to everyone)
shared_pages = [
    st.Page("pages/00_Home.py", title="Home", icon="🏠"),
    st.Page("pages/01_Login.py", title="Login", icon="🔑"),
    st.Page("pages/02_Market_Prices.py", title="Market Prices", icon="📊"),
]

# Farmer pages
farmer_pages = [
    st.Page("pages/10_Farmer_Dashboard.py", title="Dashboard", icon="🏠"),
    st.Page("pages/11_Farmer_Lots.py", title="My Crop Lots", icon="🌾"),
    st.Page("pages/12_Create_Lot.py", title="Create Lot", icon="➕"),
    st.Page("pages/14_Opportunities.py", title="Opportunities", icon="🎯"),
    st.Page("pages/15_Opportunity_Comparison.py", title="Compare Options", icon="💰"),
    st.Page("pages/16_Negotiations.py", title="Negotiations", icon="🤝"),
    st.Page("pages/17_Farmer_Groups.py", title="Groups & FPO", icon="👥"),
]

# Buyer pages
buyer_pages = [
    st.Page("pages/20_Buyer_Dashboard.py", title="Dashboard", icon="🏠"),
    st.Page("pages/21_Buyer_Requirements.py", title="My Requirements", icon="📋"),
    st.Page("pages/22_Create_Requirement.py", title="Create Requirement", icon="➕"),
    st.Page("pages/23_Buyer_Matches.py", title="Matches", icon="🎯"),
    st.Page("pages/24_Buyer_Negotiations.py", title="Negotiations", icon="🤝"),
]

# Build navigation based on login state
if is_logged_in():
    user_role = get_user_role()

    if user_role == ROLE_FARMER:
        nav = st.navigation({
            "🌾 AgroConnect": shared_pages,
            "👨‍🌾 Farmer": farmer_pages,
        })
    elif user_role == ROLE_BUYER:
        nav = st.navigation({
            "🌾 AgroConnect": shared_pages,
            "🏢 Buyer": buyer_pages,
        })
    else:
        nav = st.navigation({
            "🌾 AgroConnect": shared_pages,
        })
else:
    nav = st.navigation({
        "🌾 AgroConnect": shared_pages,
    })

nav.run()
