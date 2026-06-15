
import streamlit as st
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Chat with Google Gemini!",
    page_icon=":robot_face:",
    layout="wide",
)

# Initialize Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"

# Add chat history to Streamlit session state
if "history" not in st.session_state:
    st.session_state.history = []

# Display Form Title
st.title("Chat with Google Gemini!")

# Display chat messages from history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user's next message
if prompt := st.chat_input(
    "I possess a well of knowledge. What would you like to know?"
):
    # Store and display user message
    st.session_state.history.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from Gemini
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    # Store and display assistant response
    st.session_state.history.append(
        {"role": "assistant", "content": response.text}
    )

    with st.chat_message("assistant"):
        st.markdown(response.text)
