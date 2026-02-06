import streamlit as st
from styles import apply_theme, render_header

# Apply Theme
apply_theme()
render_header()

st.markdown("# Legal Information")

tab1, tab2 = st.tabs(["🔒 Privacy Policy", "📜 Terms of Service"])

with tab1:
    st.markdown("""
    ### Privacy Policy
    **Last Updated: October 26, 2023**

    At Gin Ai, we take your privacy seriously. This Privacy Policy explains how we collect, use, and protect your personal information.

    #### 1. Information We Collect
    *   **Account Information:** When you sign up, we collect your name and email address.
    *   **Usage Data:** We collect data on how you use our AI tools to improve our services.
    *   **Generated Content:** We process the content you generate, but we do not claim ownership of it.

    #### 2. How We Use Your Information
    We use your information to provide and improve our services, communicate with you, and ensure the security of our platform.

    #### 3. Data Security
    We implement industry-standard security measures to protect your data. However, no method of transmission over the internet is 100% secure.

    #### 4. Third-Party Services
    We may use third-party services (like Google Gemini API) to provide our AI features. Please review their privacy policies.
    """)

with tab2:
    st.markdown("""
    ### Terms of Service
    **Last Updated: October 26, 2023**

    By accessing or using Gin Ai, you agree to be bound by these Terms of Service.

    #### 1. Acceptance of Terms
    By using our services, you agree to these terms. If you do not agree, please do not use our services.

    #### 2. Use of Services
    You agree to use our services only for lawful purposes and in accordance with these terms. You are responsible for all activity that occurs under your account.

    #### 3. Intellectual Property
    Gin Ai retains all rights to the platform and its code. You retain rights to the content you generate using our tools.

    #### 4. Limitation of Liability
    Gin Ai is provided "as is" without warranties of any kind. We are not liable for any damages arising from your use of our services.

    #### 5. Changes to Terms
    We may modify these terms at any time. We will notify you of any material changes.
    """)
