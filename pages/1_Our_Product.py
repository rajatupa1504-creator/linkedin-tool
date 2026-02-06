import streamlit as st
from ai_utils import generate_content
from styles import apply_theme, render_header

# Apply Theme
apply_theme()
render_header()

# Sidebar - Navigation
st.sidebar.title("🚀 Navigation")
category = st.sidebar.radio(
    "Choose a Category",
    ["Content Creation", "Profile Optimization", "Networking", "Growth & Strategy"]
)

st.markdown(f"## **{category}**")

# Default Provider is Google
provider = "google"

# Try to get API Key
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
elif "GOOGLE_API_KEY" in os.environ:
    api_key = os.environ["GOOGLE_API_KEY"]
else:
    api_key = "mock"
    st.warning("⚠️ API Key not found. Running in **Demo Mode**. Generated content will be simulated.")

# Logic for Content Creation
if category == "Content Creation":
    tool_selection = st.selectbox(
        "Select Tool",
        ["Post Generator", "Hook Generator", "Carousel Writer", "Comment Generator", "Repost Insight", "Hashtag Generator"]
    )

    st.markdown("---")
    st.subheader(f"🛠️ {tool_selection}")

    if tool_selection == "Post Generator":
        topic = st.text_input("Enter Topic")
        tone = st.selectbox("Select Tone", ["Professional", "Casual", "Inspirational", "Educational", "Controversial"])
        post_type = st.selectbox("Post Type", ["Story", "Tips/Listicle", "Personal Branding", "Case Study"])

        if st.button("Generate Post"):
            prompt = f"Write a LinkedIn post about '{topic}'. Tone: {tone}. Type: {post_type}. Make it engaging and formatted for LinkedIn."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Generated Post", result, height=300)

    elif tool_selection == "Hook Generator":
        topic = st.text_input("Enter Topic or Context")
        if st.button("Generate Hooks"):
            prompt = f"Generate 5 scroll-stopping LinkedIn hooks (first lines) for a post about: '{topic}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "Carousel Writer":
        topic = st.text_input("Enter Topic")
        num_slides = st.slider("Number of Slides", 3, 10, 5)
        if st.button("Generate Carousel Content"):
            prompt = f"Create a slide-by-slide outline for a LinkedIn carousel about '{topic}'. It should have {num_slides} slides. Include content for each slide."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Generated Carousel Content", result, height=400)

    elif tool_selection == "Comment Generator":
        post_content = st.text_area("Paste the LinkedIn Post content here")
        if st.button("Generate Comments"):
            prompt = f"Generate 3 smart, thoughtful, and engaging comments for this LinkedIn post: '{post_content}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "Repost Insight":
        original_post = st.text_area("Paste the Original Post content")
        if st.button("Generate Insight"):
            prompt = f"I want to repost this content on LinkedIn with my own insight. Generate a thoughtful introduction/insight to add on top of this repost: '{original_post}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Generated Insight", result, height=200)

    elif tool_selection == "Hashtag Generator":
        content = st.text_area("Paste your Post Content or Topic")
        if st.button("Generate Hashtags"):
            prompt = f"Generate a list of relevant, high-reach LinkedIn hashtags for this content: '{content}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

elif category == "Profile Optimization":
    tool_selection = st.selectbox(
        "Select Tool",
        ["Headline Generator", "About Section Writer", "Experience Rewriter", "Skills Suggestion", "SEO Optimizer"]
    )

    st.markdown("---")
    st.subheader(f"🛠️ {tool_selection}")

    if tool_selection == "Headline Generator":
        role = st.text_input("Role")
        industry = st.text_input("Industry")
        usp = st.text_input("Unique Value Proposition / Key Achievement")
        if st.button("Generate Headlines"):
            prompt = f"Generate 5 high-converting LinkedIn headlines for a '{role}' in '{industry}'. Key achievement/USP: '{usp}'. Use delimiters like | or emojis where appropriate."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "About Section Writer":
        background = st.text_area("Paste your Bio / Resume Summary / Key Achievements")
        target_audience = st.text_input("Who is your target audience?")
        if st.button("Write About Section"):
            prompt = f"Write a compelling 'About' section for LinkedIn based on this background: '{background}'. Target audience: '{target_audience}'. Make it storytelling-based and professional."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Generated About Section", result, height=400)

    elif tool_selection == "Experience Rewriter":
        experience = st.text_area("Paste your current job description/bullet points")
        if st.button("Rewrite Experience"):
            prompt = f"Rewrite these job experience bullet points to be achievement-focused and metric-driven (start with action verbs): '{experience}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Rewritten Experience", result, height=300)

    elif tool_selection == "Skills Suggestion":
        profile_text = st.text_area("Paste your About section or Headline")
        if st.button("Suggest Skills"):
            prompt = f"Based on this profile text, suggest 15 relevant hard and soft skills to add to LinkedIn: '{profile_text}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "SEO Optimizer":
        profile_text = st.text_area("Paste your Headline and About section")
        keywords = st.text_input("Target Keywords (comma separated)")
        if st.button("Optimize Profile"):
            prompt = f"Analyze this LinkedIn profile text for SEO based on these keywords: '{keywords}'. Suggest improvements and where to place keywords: '{profile_text}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

elif category == "Networking":
    tool_selection = st.selectbox(
        "Select Tool",
        ["Connection Request", "Cold DM Writer", "Follow-up Generator", "Reply Assistant"]
    )

    st.markdown("---")
    st.subheader(f"🛠️ {tool_selection}")

    if tool_selection == "Connection Request":
        recipient_role = st.text_input("Recipient's Role/Title")
        shared_context = st.text_input("Shared Interest, Event, or Group")
        if st.button("Generate Note"):
            prompt = f"Write 3 personalized LinkedIn connection request notes (under 300 chars) for a '{recipient_role}'. Shared context: '{shared_context}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "Cold DM Writer":
        goal = st.selectbox("Goal", ["Sales", "Hiring", "Collaboration", "Networking"])
        target_profile = st.text_area("Recipient's Profile Summary / Description")
        if st.button("Generate Cold DM"):
            prompt = f"Write a cold DM for LinkedIn with the goal of '{goal}'. Target profile summary: '{target_profile}'. Keep it concise, personalized, and value-driven."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Generated DM", result, height=300)

    elif tool_selection == "Follow-up Generator":
        last_message = st.text_area("Context (What was your last message/interaction?)")
        if st.button("Generate Follow-up"):
            prompt = f"Write a polite and professional follow-up message for LinkedIn based on this context: '{last_message}'. Don't be pushy."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Generated Follow-up", result, height=200)

    elif tool_selection == "Reply Assistant":
        incoming_message = st.text_area("Paste the incoming message")
        intent = st.text_input("How do you want to respond? (e.g., politely decline, accept meeting, ask for more info)")
        if st.button("Generate Reply"):
            prompt = f"Draft a professional LinkedIn reply to this message: '{incoming_message}'. Intent of reply: '{intent}'."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.text_area("Generated Reply", result, height=200)

elif category == "Growth & Strategy":
    tool_selection = st.selectbox(
        "Select Tool",
        ["30 Post Ideas", "Brand Positioning", "Content Calendar", "Audience Pain Points"]
    )

    st.markdown("---")
    st.subheader(f"🛠️ {tool_selection}")

    if tool_selection == "30 Post Ideas":
        niche = st.text_input("Your Niche / Industry")
        if st.button("Generate Ideas"):
            prompt = f"Generate 30 engaging LinkedIn post ideas for the '{niche}' niche. Categorize them by themes."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "Brand Positioning":
        skills = st.text_input("Top 3 Skills")
        values = st.text_input("Core Values")
        audience = st.text_input("Target Audience")
        if st.button("Generate Positioning"):
            prompt = f"Create a personal brand positioning statement for someone with skills in '{skills}', values '{values}', targeting '{audience}'. Also suggest a tagline."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "Content Calendar":
        topics = st.text_input("Core Topics (comma separated)")
        frequency = st.selectbox("Posting Frequency", ["Daily", "3 times a week", "Weekly"])
        if st.button("Generate Calendar"):
            prompt = f"Create a '{frequency}' content calendar for LinkedIn covering these topics: '{topics}'. Provide a 4-week plan."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)

    elif tool_selection == "Audience Pain Points":
        audience_desc = st.text_input("Describe your Target Audience")
        if st.button("Identify Pain Points"):
            prompt = f"Identify 10 deep pain points and struggles of '{audience_desc}' that I can address in my LinkedIn content."
            with st.spinner("Add magic to your creative workflow..."):
                result = generate_content(prompt, api_key, provider)
                st.write(result)
