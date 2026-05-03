import streamlit as st
from llm_helper import generate_content

st.set_page_config(page_title="AI Content Generator", layout="centered")

st.title("✍️ AI Content Generator")

topic = st.text_input("Enter your topic")

tone = st.selectbox(
    "Select Tone",
    ["formal", "casual", "technical", "creative"]
)

content_type = st.selectbox(
    "Select Output Type",
    ["Blog Post", "LinkedIn Post", "Twitter/X Thread"]
)

word_limit = st.slider("Word Limit", 50, 10000, 300)

if st.button("Generate Content"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating content..."):
            result = generate_content(topic, tone, content_type, word_limit)
            st.success("Done!")
            st.write(result)