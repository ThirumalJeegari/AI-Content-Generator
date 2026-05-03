import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_content(topic, tone, content_type, word_limit):
    prompt = f"""
You are an expert content writer.

Write a {content_type} on the topic: "{topic}"

Requirements:
- Tone: {tone}
- Word limit: {word_limit} words
- Make it engaging and high quality
- If Twitter thread, create multiple tweets with numbering
- If LinkedIn, make it professional and structured
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional content writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content