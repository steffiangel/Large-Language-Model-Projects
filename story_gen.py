from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

# Set your Google API key
GOOGLE_API_KEY = "AIzaSyAMaomWdpLnofD7XJ5gZeMIwKqYqwYSa6M"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load the Gemini model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(prompt):
    response = chat.send_message(prompt, stream=True)
    return response

st.set_page_config(page_title="Story Generation")
st.header("Gemini Pro Story Generation Application")

# Initial chat history based on session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_prompt = st.text_input("Enter a story prompt:", key='input_prompt')
submit = st.button('Generate Story')

if submit and input_prompt:
    response = get_gemini_response(input_prompt)
    generated_story = ""
    for chunk in response:
        generated_story += chunk.text
    
    # Add the prompt and generated story to session history
    st.session_state['chat_history'].append(('You', input_prompt))
    st.session_state['chat_history'].append(('Bot', generated_story))
    st.subheader("Generated Story:")
    st.write(generated_story)

st.subheader("Chat History:")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
