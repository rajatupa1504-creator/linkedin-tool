import streamlit as st

def apply_agency_theme():
    """
    Applies the Instagram Agency theme to the Streamlit app.
    Sets page config and injects custom CSS.
    """
    # Page Config
    st.set_page_config(page_title="Instagram Marketing Agency", page_icon="📈", layout="wide")

    # Custom CSS for Agency Theme
    st.markdown("""
    <style>
        /* Global Background */
        .stApp {
            background-color: #F8F9FA; /* Light Gray/White */
            color: #333333;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }

        /* Text Color Override */
        h1, h2, h3, h4, h5, h6, p, label, div, span, li {
            color: #333333;
        }

        /* Headers */
        h1 {
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        h2 {
            font-weight: 700;
            color: #262626 !important;
        }
        h3 {
            font-weight: 600;
            color: #262626 !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #ffffff; /* White Sidebar */
            border-right: 1px solid #dbdbdb;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%);
            color: white !important;
            border-radius: 8px; /* Slightly less rounded for professional feel */
            border: none;
            padding: 12px 28px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
            opacity: 0.95;
        }

        /* Inputs */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div {
            background-color: #ffffff;
            color: #333333;
            border-radius: 8px;
            border: 1px solid #dbdbdb;
            padding: 10px;
        }
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #bc1888;
            box-shadow: 0 0 0 1px #bc1888;
        }

        /* Card Style for Services/Features */
        .service-card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 12px;
            border: 1px solid #dbdbdb;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            transition: transform 0.3s, box-shadow 0.3s;
            height: 100%;
        }
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            border-color: #e1306c; /* Instagram Pink */
        }

        /* Testimonial Card */
        .testimonial-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            border-left: 4px solid #833AB4; /* Purple Accent */
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            font-style: italic;
        }

        /* Footer */
        .footer-container {
            background-color: #fafafa;
            padding: 40px 0;
            border-top: 1px solid #dbdbdb;
            text-align: center;
            margin-top: 50px;
        }

        /* Utility */
        .text-center {
            text-align: center;
        }
        .section-padding {
            padding: 60px 0;
        }

    </style>
    """, unsafe_allow_html=True)
