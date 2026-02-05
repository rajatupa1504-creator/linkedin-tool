import google.generativeai as genai
from openai import OpenAI
import os
import streamlit as st

def generate_content(prompt, api_key=None, provider='google'):
    """
    Generates content using the specified AI provider.

    Args:
        prompt (str): The prompt to send to the AI.
        api_key (str): The API key for the provider. If None, tries to fetch from secrets or env.
        provider (str): 'google' or 'openai'.

    Returns:
        str: The generated text content.
    """
    # Try to fetch key from Streamlit secrets or Environment Variables if not provided
    if not api_key:
        if provider == 'google':
            try:
                # Try Streamlit secrets first
                api_key = st.secrets["GOOGLE_API_KEY"]
            except (FileNotFoundError, KeyError):
                # Fallback to Environment Variable
                api_key = os.environ.get("GOOGLE_API_KEY")

        # If still no key, return error
        if not api_key:
             return "Error: API Key not configured. Please set GOOGLE_API_KEY in .streamlit/secrets.toml or environment variables."

    try:
        if provider == 'google':
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text

        elif provider == 'openai':
            client = OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specialized in LinkedIn content creation and optimization."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content

        else:
            return "Error: Invalid provider specified."

    except Exception as e:
        return f"Error generating content: {str(e)}"
