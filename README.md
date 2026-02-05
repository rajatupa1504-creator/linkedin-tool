# LinkedIn AI Assistant

A Streamlit-based AI tool for LinkedIn content creation, profile optimization, and growth strategy.

## Features

*   **Content Creation:** Post Generator, Hook Generator, Carousel Writer, etc.
*   **Profile Optimization:** Headline Generator, About Section Writer, SEO Optimizer.
*   **Networking:** Connection Request Generator, Cold DM Writer.
*   **Growth & Strategy:** Post Ideas, Content Calendar, Brand Positioning.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure API Key:**
    *   Create a folder named `.streamlit` in the root directory.
    *   Create a file named `secrets.toml` inside `.streamlit`.
    *   Add your Google Gemini API Key:
        ```toml
        GOOGLE_API_KEY = "your_api_key_here"
        ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```
