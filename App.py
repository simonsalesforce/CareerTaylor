import streamlit as st
import random

st.set_page_config(page_title="Career Chat", layout="centered")

st.title("💼 Career Advice Bot")
st.subheader("Now with 42% more emotional intensity than HR would recommend.")

st.markdown("_Example: 'I'm stuck choosing between two jobs' or 'I want to quit my job'_")
user_input = st.text_input("What's your career question?")

responses = [
    {
        "keywords": ["leave", "quit", "resign"],
        "response": "If you've been clocking in like it's a bad romance on repeat, maybe it’s time to ask: is this job really the one? Because staying just to keep the peace is how you end up screaming internally, we are never, ever getting back together — with your motivation. You deserve a role that loves you back. Right now? Feels like you’re just playing the part."
    },
    {
        "keywords": ["didn't get", "rejected", "failed", "lost"],
        "response": "Oof. That one stings. You dressed for it, prepared, walked in with confidence, only to be met with silence. Shake it off. Seriously. This doesn’t mean you’re not qualified — it just wasn’t your spotlight moment. Next time? You'll come back stronger, with red lipstick and a blank space — ready to write their name."
    },
    {
        "keywords": ["freelance", "self-employed", "contract", "independent"],
        "response": "Freelancing isn’t for the faint-hearted. It’s late nights, wild ideas, and the occasional existential crisis. But if every morning feels like you’re showing up in a place where you don’t even recognize yourself anymore, well... maybe it's time to start your own era. Sometimes the best thing you can do is step out in style."
    },
    {
        "keywords": ["wrong career", "regret", "mistake"],
        "response": "Hey — life’s not linear. You could’ve sworn this path would be forever, and now it feels like a bridge you can’t uncross. But even if it was bad blood, it still taught you something. Careers, like relationships, don’t always go to plan. Just don’t stay stuck playing a part in someone else’s love story."
    },
    {
        "keywords": ["lost", "everyone", "behind", "late", "direction"],
        "response": "It’s easy to believe they’ve all got it figured out, but remember: even the ones who look polished on LinkedIn sometimes cry in the bathroom during lunch. You're not behind — you’re just in a different verse. And honestly? You’re doing better than you think. It’s me, hi. You’re the solution. It's you."
    }
]

def match_response(question):
    question_lower = question.lower()
    for r in responses:
        if any(k in question_lower for k in r["keywords"]):
            return r["response"]
    return random.choice(responses)["response"]

if user_input:
    st.markdown("---")
    st.subheader("Career Advice:")
    st.write(match_response(user_input))
    if st.button("Ask Again"):
        st.experimental_rerun()
