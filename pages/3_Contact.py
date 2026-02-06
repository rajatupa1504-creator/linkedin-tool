import streamlit as st
from styles import apply_theme, render_header

# Apply Theme
apply_theme()
render_header()

st.markdown("# Contact Us")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    ### Let's Chat 💬
    Have questions about our enterprise plans? Need help optimizing your profile?
    Our team is here to help you succeed on LinkedIn.

    <br>
    """, unsafe_allow_html=True)

    st.info("""
    **📍 Headquarters**
    123 Innovation Drive,
    San Francisco, CA 94105
    """)

    st.info("""
    **📧 Email Support**
    support@ginai-linkedin.com
    (We typically reply within 24 hours)
    """)

    st.markdown("### Connect with us")
    st.markdown("🌐 [LinkedIn Page](#)")
    st.markdown("🐦 [Twitter / X](#)")

with col2:
    st.markdown("""
    <div style="background-color: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1);">
    """, unsafe_allow_html=True)

    st.subheader("Send us a message")

    with st.form("contact_form"):
        name = st.text_input("Your Name", placeholder="John Doe")
        email = st.text_input("Your Email", placeholder="john@company.com")
        subject = st.selectbox("Topic", ["General Inquiry", "Support", "Enterprise/Sales", "Feedback"])
        message = st.text_area("Message", placeholder="How can we help you?")

        submitted = st.form_submit_button("Send Message 🚀")
        if submitted:
            if name and email and message:
                st.success(f"Thanks {name}! Your message has been sent to our team.")
                st.balloons()
            else:
                st.warning("Please fill in all fields.")

    st.markdown("</div>", unsafe_allow_html=True)
