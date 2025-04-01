import streamlit as st
import openai
import os

st.set_page_config(page_title="Career Chat", layout="centered")

st.title("💼 Career Advice Bot")
st.subheader("Helping you define your Era")

st.markdown("_Example: 'I'm stuck choosing between two jobs' or 'I want to quit my job'_")
user_input = st.text_input("What's your career question?")

def get_llm_response(question):
    prompt = f"""
You are a dramatic, emotionally insightful careers adviser who secretly responds using lyrics and references from popular Taylor Swift songs. Your audience is adults pretending to build a career tool for teenagers. 

Respond to the following career question with creative, heartfelt advice. You must include at least one line or phrase clearly inspired by a well-known Taylor Swift song. Do not mention Taylor Swift or the name of the song. Just subtly embed the lyrics within your answer.

Career question: "{question}"
"""

    openai.api_key = os.getenv("GROQ_API_KEY")
    openai.api_base = "https://api.groq.com/openai/v1"

    try:
        response = openai.ChatCompletion.create(
            model="mixtral-8x7b",
            messages=[
                {"role": "system", "content": "You are a poetic career adviser who references pop lyrics in serious-sounding career advice."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Something went wrong: {str(e)}"

if user_input:
    st.markdown("---")
    st.subheader("Career Advice:")
    with st.spinner("Thinking in metaphors and glitter..."):
        st.write(get_llm_response(user_input))
    if st.button("Ask Again"):
        st.experimental_rerun()