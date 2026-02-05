import google.generativeai as genai
from openai import OpenAI
import os

def generate_content(prompt, api_key, provider='google'):
    """
    Generates content using the specified AI provider.

    Args:
        prompt (str): The prompt to send to the AI.
        api_key (str): The API key for the provider.
        provider (str): 'google' or 'openai'.

    Returns:
        str: The generated text content.
    """
    if not api_key:
        return "Error: Please provide an API Key."

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
