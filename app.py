import streamlit as st
from styles import apply_theme, render_header

# Apply Theme
apply_theme()
render_header()

# Hero Section
st.markdown("""
<div style="text-align: center; padding: 4rem 0;">
    <h1 style="font-size: 3.5rem; font-weight: 800; margin-bottom: 1rem;">
        Supercharge Your <span style="background: -webkit-linear-gradient(left, #fff, #A91079); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">LinkedIn Presence</span> with AI
    </h1>
    <p style="font-size: 1.2rem; opacity: 0.8; max-width: 700px; margin: 0 auto 2rem auto; line-height: 1.6;">
        The all-in-one platform to automate content, optimize your profile,
        and grow your network 10x faster using advanced AI algorithms.
    </p>
</div>
""", unsafe_allow_html=True)

# Hero CTA Buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Start Growing Free 🚀", use_container_width=True):
        st.switch_page("pages/1_Our_Product.py")

# Core Services Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; margin-bottom: 2rem;'>Core Services</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-bottom: 3rem; opacity: 0.8;'>Unlock your full potential with our suite of AI-powered tools designed specifically for LinkedIn professionals.</p>", unsafe_allow_html=True)

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📝 Content Creation</h3>
        <p style="opacity: 0.8;">Viral Post Generator, Hook Generator, Carousel Writer, and more. Create engaging content in seconds that stops the scroll.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>🤝 Networking</h3>
        <p style="opacity: 0.8;">Smart Connection Outreach, Cold DM Writer, and Reply Assistant. Build meaningful connections that convert.</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="feature-card">
        <h3>👤 Profile Optimization</h3>
        <p style="opacity: 0.8;">Headline Generator, About Section Writer, and SEO Optimizer. Stand out to recruiters and clients instantly.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-card">
        <h3>📈 Growth & Strategy</h3>
        <p style="opacity: 0.8;">30 Post Ideas, Content Calendar, and Brand Positioning. Data-driven growth tactics to scale your brand.</p>
    </div>
    """, unsafe_allow_html=True)

# Social Proof Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h4 style='text-align: center; opacity: 0.6; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 2rem;'>Trusted by professionals at top companies</h4>", unsafe_allow_html=True)

sp_cols = st.columns(5)
companies = ["TechCorp", "GlobalNet", "StartUp.io", "LuxBrand", "FinGroup"]
icons = ["🛡️", "🌐", "⚡", "💎", "💼"]

for col, company, icon in zip(sp_cols, companies, icons):
    with col:
        st.markdown(f"<div style='text-align: center; font-weight: bold; opacity: 0.7; font-size: 1.2rem;'>{icon} {company}</div>", unsafe_allow_html=True)

# Footer CTA
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="background-color: rgba(255,255,255,0.05); padding: 3rem; border-radius: 20px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
    <h2 style="margin-bottom: 1rem;">Ready to transform your career?</h2>
    <p style="opacity: 0.8; margin-bottom: 2rem;">Join thousands of professionals using AI to stand out, get hired, and close deals faster than ever before.</p>
</div>
""", unsafe_allow_html=True)

# Final Footer Links
st.markdown("<br><br>", unsafe_allow_html=True)
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1:
    st.markdown("**✨ Gin Ai - Linkedin**")
with f_col2:
    st.markdown("<div style='text-align: center; opacity: 0.5;'>© 2024 Gin Ai Platform</div>", unsafe_allow_html=True)
with f_col3:
    st.markdown("<div style='text-align: right; opacity: 0.8;'>Privacy Policy • Terms</div>", unsafe_allow_html=True)
