import streamlit as st
import openai
import os

# Page config
st.set_page_config(page_title="Career Chat", layout="centered")
st.markdown("<small>Today's Date: <b>1st April</b> 2025</small>", unsafe_allow_html=True)
st.title("💼 Career Advice Bot")
st.subheader("Helping you define your Era")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "new_input" not in st.session_state:
    st.session_state.new_input = None
if "trigger_rerun" not in st.session_state:
    st.session_state.trigger_rerun = False

# Function to get a Swiftie-flavored response
def get_llm_response(question):
    prompt = f"""You are a thoughtful, emotionally insightful careers adviser who gives helpful and supportive guidance to teenagers exploring their future. 

You respond in a warm, lyrical tone — blending in a few well-known Taylor Swift lyrics and references, but never overwhelming the user with them. 

Your top priority is to give genuinely useful advice. This includes:  
- Suggesting relevant job paths or industries  
- Mentioning helpful school subjects, training, or qualifications  
- Encouraging exploration or reflection  
- Being realistic but kind about next steps  

You’re allowed to include one or two clearly recognizable lyrics from Taylor Swift’s most popular songs (such as *Shake it Off*, *You Belong With Me*, *It’s Me, Hi, I’m the Problem*, etc), but don’t use quotation marks, and never say her name or the song titles.

Speak like a mentor who understands uncertainty and wants the user to feel hopeful and curious.

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

# If new input exists from last run, process it
if st.session_state.new_input:
    with st.spinner("Thinking in metaphors and glitter..."):
        answer = get_llm_response(st.session_state.new_input)
        st.session_state.chat_history.append((st.session_state.new_input, answer))
    st.session_state.new_input = None  # Clear for next question

# Show the full conversation history
if st.session_state.chat_history:
    st.markdown("---")
    for q, a in st.session_state.chat_history:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
        st.markdown("---")

# Input label adjusts depending on whether it’s the first question
input_label = "What's your career question?" if len(st.session_state.chat_history) == 0 else "Ask another question:"

# Input form at bottom
with st.form("follow_up_form"):
    user_input = st.text_input(label=input_label, key="input_text")
    submitted = st.form_submit_button("💬 Submit")

    if submitted and user_input:
        st.session_state.new_input = user_input
        if "input_text" in st.session_state:
            del st.session_state["input_text"]  # ✅ Properly clear input field
        st.session_state.trigger_rerun = True

# Trigger rerun if needed (after setting new input)
if st.session_state.trigger_rerun:
    st.session_state.trigger_rerun = False
    st.rerun()

# Optional: Clear chat
if st.button("🧹 Clear conversation"):
    st.session_state.chat_history = []
    if "input_text" in st.session_state:
        del st.session_state["input_text"]
    st.rerun()
