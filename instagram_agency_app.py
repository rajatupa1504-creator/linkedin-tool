import streamlit as st
from agency_styles import apply_agency_theme

# Apply Theme
apply_agency_theme()

# --- HERO SECTION ---
with st.container():
    st.markdown("<div style='text-align: center; padding-top: 2rem; padding-bottom: 3rem;'>", unsafe_allow_html=True)
    st.markdown("""
    <h1 style='font-size: 3.5rem; margin-bottom: 1rem;'>
        Explode Your Sales with Expert <br> Instagram Marketing
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p style='font-size: 1.25rem; color: #666; max-width: 800px; margin: 0 auto 2.5rem auto; line-height: 1.6;'>
        We turn your Instagram traffic into loyal customers and booked calls.
        Tailored strategies designed specifically for Small & Medium Enterprises to grow brand authority and revenue.
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([1, 1.5, 0.5, 1.5, 1])
    with col2:
        if st.button("📅 Book Free Strategy Call", use_container_width=True):
            st.toast("Redirecting to booking calendar...")
    with col4:
        if st.button("🚀 Get Free Audit", use_container_width=True):
             st.toast("Scroll down to request your audit!")

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- ABOUT US ---
with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Our Team Brainstorming", use_container_width=True)
    with col2:
        st.markdown("<div style='padding: 2rem;'>", unsafe_allow_html=True)
        st.markdown("## Who We Are")
        st.markdown("""
        <p style='font-size: 1.1rem; line-height: 1.6; color: #444;'>
        We are a dedicated team of Instagram growth experts passionate about helping SMEs thrive in the digital age.
        We understand that likes and followers are vanity metrics if they don't convert into sales.
        <br><br>
        Our mission is simple: <strong>To build trust-based marketing systems that generate consistent leads and measurable ROI for your business.</strong>
        We don't just post content; we craft strategies that speak directly to your ideal customer.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# --- SERVICES SECTION ---
st.markdown("<div class='text-center section-padding'>", unsafe_allow_html=True)
st.markdown("## Our Services")
st.markdown("<p style='color: #666;'>Comprehensive solutions to scale your Instagram presence</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 2rem; margin-bottom: 1rem;">✨</div>
        <h3>Account Setup & Optimization</h3>
        <p style="color: #666; font-size: 0.95rem;">
            We optimize your bio, highlights, and profile structure to convert visitors into followers and leads instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 2rem; margin-bottom: 1rem;">📱</div>
        <h3>Content Strategy & Reels</h3>
        <p style="color: #666; font-size: 0.95rem;">
            Viral-worthy Reels and engaging carousel posts tailored to your niche to skyrocket your organic reach.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🎯</div>
        <h3>Paid Ads Management</h3>
        <p style="color: #666; font-size: 0.95rem;">
            Laser-focused ad campaigns that target your ideal customers and deliver high ROI without wasting budget.
        </p>
    </div>
    """, unsafe_allow_html=True)

col4, col5 = st.columns([1, 1])
with col4:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 2rem; margin-bottom: 1rem;">🔥</div>
        <h3>Lead Generation Campaigns</h3>
        <p style="color: #666; font-size: 0.95rem;">
            Automated DM funnels and lead magnet strategies to capture emails and phone numbers 24/7.
        </p>
    </div>
    """, unsafe_allow_html=True)
with col5:
    st.markdown("""
    <div class="service-card">
        <div style="font-size: 2rem; margin-bottom: 1rem;">📊</div>
        <h3>Analytics & Reporting</h3>
        <p style="color: #666; font-size: 0.95rem;">
            Transparent monthly reports showing exactly how our efforts are translating into growth and sales.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- WHY CHOOSE US ---
st.markdown("<div style='background-color: #f0f2f5; padding: 4rem 2rem; border-radius: 20px;'>", unsafe_allow_html=True)
st.markdown("<h2 class='text-center'>Why Partner With Us?</h2>", unsafe_allow_html=True)

wc_col1, wc_col2, wc_col3 = st.columns(3)
with wc_col1:
    st.markdown("<h3 style='text-align:center; color: #833AB4 !important;'>📈 Data-Driven</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #555;'>We don't guess. We use real-time data to pivot and optimize for the best results.</p>", unsafe_allow_html=True)
with wc_col2:
    st.markdown("<h3 style='text-align:center; color: #C13584 !important;'>💰 ROI-Focused</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #555;'>Your investment must yield returns. We focus on metrics that matter: Revenue and Leads.</p>", unsafe_allow_html=True)
with wc_col3:
    st.markdown("<h3 style='text-align:center; color: #E1306C !important;'>🤝 SME Friendly</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color: #555;'>Pricing and strategies specifically designed for the budgets and goals of small businesses.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- PROCESS SECTION ---
st.markdown("## Our Proven Process")
st.markdown("1. **Audit** - We analyze your current state.")
st.markdown("2. **Strategy** - We build a roadmap.")
st.markdown("3. **Execution** - We create and post.")
st.markdown("4. **Growth** - You see the numbers climb.")
st.markdown("5. **Reporting** - We review and refine.")
st.progress(100) # Just a visual bar

st.markdown("<br><br>", unsafe_allow_html=True)

# --- RESULTS / BENEFITS ---
r_col1, r_col2 = st.columns(2)
with r_col1:
    st.markdown("## Real Results for Real Businesses")
    st.markdown("""
    <ul style='font-size: 1.2rem; line-height: 2; list-style-type: none;'>
        <li>✅ <strong>Increased Reach:</strong> Get seen by thousands of new potential customers.</li>
        <li>✅ <strong>More Leads:</strong> Turn passive scrollers into active inquiries.</li>
        <li>✅ <strong>Brand Authority:</strong> Become the go-to expert in your local niche.</li>
    </ul>
    """, unsafe_allow_html=True)
with r_col2:
     st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Growth Analytics", use_container_width=True)

st.markdown("---")

# --- TESTIMONIALS ---
st.markdown("<h2 class='text-center'>What Our Clients Say</h2>", unsafe_allow_html=True)
t_col1, t_col2 = st.columns(2)
with t_col1:
    st.markdown("""
    <div class="testimonial-card">
        "Since working with the agency, our boutique's online sales have doubled! The content is beautiful and actually converts."
        <br><br><strong>— Sarah M., Boutique Owner</strong>
    </div>
    """, unsafe_allow_html=True)
with t_col2:
    st.markdown("""
    <div class="testimonial-card">
        "I was skeptical about Instagram ads, but they made it work. We're getting 10+ booked appointments a week now."
        <br><br><strong>— Mike R., Personal Trainer</strong>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- LEAD CAPTURE SECTION ---
st.markdown("<div style='background-color: #ffffff; padding: 3rem; border-radius: 15px; border: 1px solid #ddd; box-shadow: 0 4px 12px rgba(0,0,0,0.1);'>", unsafe_allow_html=True)
st.markdown("<h2 class='text-center'>Ready to Grow? Get Your Free Audit</h2>", unsafe_allow_html=True)

with st.form("lead_capture_form"):
    lc_col1, lc_col2 = st.columns(2)
    with lc_col1:
        name = st.text_input("Full Name", placeholder="John Doe")
        phone = st.text_input("Phone Number", placeholder="+1 234 567 8900")
    with lc_col2:
        business_name = st.text_input("Business Name", placeholder="My Awesome Biz")
        email = st.text_input("Email Address", placeholder="john@example.com")

    notes = st.text_area("Tell us about your goals", placeholder="I want to increase sales by 20%...")

    submitted = st.form_submit_button("🚀 Send Me My Free Strategy Plan", use_container_width=True)
    if submitted:
        if name and email:
            st.success(f"Thanks {name}! We'll be in touch shortly at {email}.")
        else:
            st.error("Please fill in at least your Name and Email.")

st.markdown("<div style='text-align: center; margin-top: 1.5rem;'>", unsafe_allow_html=True)
st.markdown("Or chat with us directly:")
col_cta1, col_cta2 = st.columns(2)
with col_cta1:
    st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat%20Us-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/)")
with col_cta2:
    st.markdown("[![Instagram](https://img.shields.io/badge/Instagram-DM%20Us-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/)")
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- FAQ SECTION ---
st.markdown("## Frequently Asked Questions")
with st.expander("Do you work with small budgets?"):
    st.write("Yes! We specialize in working with SMEs and have packages designed for various budget levels.")
with st.expander("How long does it take to see results?"):
    st.write("While some changes (like profile optimization) have immediate effects, sustainable growth typically gains momentum within 2-3 months.")
with st.expander("Do I need to provide the photos/videos?"):
    st.write("It helps if you have raw assets, but we can also use stock footage, create graphics, or guide you on how to shoot simple content on your phone.")
with st.expander("Is there a long-term contract?"):
    st.write("We offer flexible month-to-month options as well as discounted 6-month retainers. We believe our results should keep you with us, not a contract.")

# --- FOOTER ---
st.markdown("""
<div class="footer-container">
    <h3>Instagram Marketing Agency</h3>
    <p>Helping businesses grow, one post at a time.</p>
    <p>📍 New York, NY | 📧 hello@agency.com | 📞 (555) 123-4567</p>
    <p style="font-size: 0.8rem; color: #999;">© 2024 Instagram Marketing Agency. All rights reserved.</p>
    <p>
        <a href="#" style="color: #666; text-decoration: none;">Privacy Policy</a> |
        <a href="#" style="color: #666; text-decoration: none;">Terms of Service</a>
    </p>
</div>
""", unsafe_allow_html=True)
