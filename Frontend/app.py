import streamlit as st
from adk_client import ensure_session, run_turn

st.set_page_config(page_title="StudyPal", layout="wide")

# --- simple state ---
if "user_id" not in st.session_state:
    st.session_state.user_id = "demo_user"
if "session_id" not in st.session_state:
    st.session_state.session_id = "s_flashcards"

# Sidebar to pick feature
feature = st.sidebar.selectbox(
    "Feature",
    ["Flashcards", "Summarize", "Quiz", "Study Plan"]
)

# Map feature to your agent folder names
AGENT_MAP = {
    "Flashcards": "flashcard_agent",
    "Summarize": "summarizer_agent",
    "Quiz": "quiz_agent",
    "Study Plan": "planner_agent",
}

app_name = AGENT_MAP[feature]

ensure_session(app_name, st.session_state.user_id, st.session_state.session_id)

st.title(f"{feature}")

if feature == "Flashcards":
    text = st.text_area("Paste your notes or textbook excerpt")
    num = st.number_input("Number of cards", 1, 50, 5)
    if st.button("Generate"):
        prompt = f"Generate {num} flashcards from these notes:\n{text}"
        events = run_turn(app_name, st.session_state.user_id, st.session_state.session_id, prompt)

        # find tool response or final text
        cards = None
        final_text = ""
        for ev in events:
            parts = ev.get("content", {}).get("parts", [])
            for p in parts:
                # function_response holds your tool output if the tool returned JSON
                if "functionResponse" in p:
                    resp = p["functionResponse"]["response"]
                    cards = resp.get("result")
                if "text" in p and p["text"]:
                    final_text = p["text"]

        if cards:
            st.success("Flashcards:")
            for i, c in enumerate(cards, 1):
                q = c.get("question") or list(c.keys())[0]
                a = c.get("answer") or list(c.values())[0]
                with st.expander(f"Card {i}: {q}"):
                    st.write(a)
        else:
            st.info(final_text or "No structured flashcards returned.")

# Repeat similar blocks for Summarize / Quiz / Study Plan using the right prompts
