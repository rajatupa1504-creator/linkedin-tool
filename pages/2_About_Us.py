import streamlit as st
from styles import apply_theme, render_header

# Apply Theme
apply_theme()
render_header()

st.markdown("# About Us")

# Mission Section
st.markdown("""
<div style="background-color: rgba(255,255,255,0.05); padding: 2rem; border-radius: 15px; margin-bottom: 2rem;">
    <h3 style="color: #A91079 !important;">Our Mission 🚀</h3>
    <p style="font-size: 1.1rem; line-height: 1.6;">
        At <strong>Gin Ai</strong>, we believe that professional growth shouldn't be limited by writer's block or lack of time.
        Our mission is to empower every professional to tell their story, build their brand, and connect with opportunities
        using the power of Generative AI. We are democratizing personal branding for the modern workforce.
    </p>
</div>
""", unsafe_allow_html=True)

# Values Section
st.markdown("### Why Professionals Choose Gin Ai")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>⚡ Speed & Efficiency</h4>
        <p>Generate weeks of high-quality content in just minutes. Focus on engagement, not creation.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>🧠 Smart AI Models</h4>
        <p>Our models are fine-tuned specifically for LinkedIn's professional tone and viral algorithms.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>🔒 Privacy First</h4>
        <p>Your data is yours. We prioritize security and never use your personal data to train public models.</p>
    </div>
    """, unsafe_allow_html=True)

# Team Section (Placeholder)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### Meet the Team")

t_col1, t_col2, t_col3 = st.columns(3)

with t_col1:
    st.markdown("### 👩‍💻")
    st.markdown("**Sarah Jenkins**")
    st.caption("CEO & Founder")
    st.write("Ex-LinkedIn Product Manager with a passion for creator economy.")

with t_col2:
    st.markdown("### 👨‍🔬")
    st.markdown("**David Chen**")
    st.caption("CTO")
    st.write("AI Researcher specializing in NLP and Large Language Models.")

with t_col3:
    st.markdown("### 🚀")
    st.markdown("**Marcus Johnson**")
    st.caption("Head of Growth")
    st.write("Growth hacker who scaled 3 SaaS startups to $10M ARR.")
