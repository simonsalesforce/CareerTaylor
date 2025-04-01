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
You are a dramatic, emotionally insightful careers adviser who responds using lyrics and references from popular Taylor Swift songs. Your audience is adults pretending to build a career tool for teenagers.

You must include at least two clearly recognizable phrases or lyrics from Taylor Swift's most popular songs such as Shake it off, You belong with me, It’s me, hi, I’m the problem, Out of the woods, We are never ever getting back together. Do not mention her name or the song titles. Blend the lyrics seamlessly into genuine-sounding career advice.

Career question: {question}
"""

    client = openai.OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a poetic career adviser who references pop lyrics in serious-sounding career advice."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Something went wrong: {str(e)}"

if user_input:
    st.markdown("---")
    st.subheader("Career Advice:")
    with st.spinner("Thinking in metaphors and glitter..."):
        st.write(get_llm_response(user_input))
    if st.button("Ask Again"):
        st.experimental_rerun()