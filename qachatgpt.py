from dotenv import load_dotenv
#from langchain.output_parsers import StrOutputParser
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
GOOGLE_API_KEY = "AIzaSyAMaomWdpLnofD7XJ5gZeMIwKqYqwYSa6M"
#genai.configure(api_keys=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=GOOGLE_API_KEY)
#funtion to load gemini model
model=genai.GenerativeModel("gemini-1.5-flash")
chat=model.start_chat(history=[])
#parser=StrOutputParser()

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A")
st.header("Gemini 1.5 Flash LLM Application Lab-2")

#intial chat history based on session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("Input: ",key='input')
submit=st.button('Ask me questions: ')

if submit and input:
    response=get_gemini_response(input)
    #add qusetion and respone to session history
    st.session_state['chat_history'].append(( 'You',input))
    st.subheader("The response is :")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(( 'Bot',chunk.text))
st.subheader("The chat history is: ")


for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")