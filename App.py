import streamlit as st
import openai
import os

# Page config
st.set_page_config(page_title="Career Chat", layout="centered")
st.markdown("<small>Today's Date: <b>1st April</b> 2025</small>", unsafe_allow_html=True)
st.title("💼 Career Advice Bot")
st.subheader("Helping you define your Era")

# Example prompt
st.markdown("_Example: 'I think I want to be a pilot' or 'I like animals'_")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("What's your career question?", key="career_input")

# LLM call
def get_llm_response(question):
    prompt = f"""
You are a dramatic, emotionally insightful careers adviser who responds using lyrics and references from popular Taylor Swift songs. Your audience is adults pretending to build a career tool for teenagers.

You must include at least two clearly recognizable phrases or lyrics from Taylor Swift's most popular songs such as Shake it off, You belong with me, It’s me, hi, I’m the problem, Out of the woods, We are never ever getting back together. Do not mention her name or the song titles. Do not put any lyrics in quotation marks. Blend the lyrics seamlessly into genuine-sounding career advice.

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

# On submit
if user_input:
    with st.spinner("Thinking in metaphors and glitter..."):
        response = get_llm_response(user_input)
        st.session_state.chat_history.append((user_input, response))
    st.session_state.career_input = ""  # Clear input field

# Display chat history
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("Your Swiftie Career Advice So Far:")
    for question, answer in st.session_state.chat_history:
        st.markdown(f"**You:** {question}")
        st.markdown(f"**Bot:** {answer}")
        st.markdown("---")

# Optional: Add clear chat button
if st.button("🧹 Clear conversation"):
    st.session_state.chat_history = []
    st.experimental_rerun()
