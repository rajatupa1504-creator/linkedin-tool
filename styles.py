import streamlit as st

def apply_theme():
    """
    Applies the MagicBrief theme to the Streamlit app.
    Sets page config and injects custom CSS.
    """
    # Page Config
    st.set_page_config(page_title="Gin Ai - Linkedin", page_icon="✨", layout="wide")

    # Custom CSS for MagicBrief Theme
    st.markdown("""
    <style>
        /* Global Background */
        .stApp {
            background-color: #2E0249; /* Deep Purple */
            color: #ffffff;
        }

        /* Text Color Override */
        h1, h2, h3, h4, h5, h6, p, label, div, span, li {
            color: #ffffff !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #570A57; /* Lighter Purple */
        }

        /* Buttons */
        .stButton > button {
            background-color: #A91079; /* Magenta/Lavender Accent */
            color: white !important;
            border-radius: 20px;
            border: none;
            padding: 10px 24px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #F806CC; /* Brighter Accent */
            transform: scale(1.05);
        }

        /* Inputs */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div {
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        /* Headers */
        header {
            background-color: transparent !important;
        }

        /* Custom Header Container */
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
            margin-bottom: 2rem;
        }

        .magic-title {
            font-size: 2.5rem;
            font-weight: 800;
            background: -webkit-linear-gradient(left, #fff, #A91079);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Card Style for Features */
        .feature-card {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
            transition: transform 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: #A91079;
        }

        /* Nav Link fix if needed (Streamlit native nav is white usually) */

    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Renders the standard header."""
    st.markdown("""
    <div class="header-container">
        <div class="magic-title">✨ Gin Ai - Linkedin</div>
    </div>
    """, unsafe_allow_html=True)
