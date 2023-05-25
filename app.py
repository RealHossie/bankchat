# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
import streamlit as st
import openai

# Load the .env file
load_dotenv()

# Get the OPENAI_API_KEY
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set the OpenAI key
openai.api_key = OPENAI_API_KEY

# Streamlit app
st.title('AI客服机器人')

knowledge_base = st.text_area("请输入你的知识库:")

question = st.text_input("请输入你的问题:")

# Initialize the session state
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = ''

if st.button('提交'):
    # Append user's question to conversation history
    st.session_state['conversation_history'] += '你: ' + question + '\n'

    # Define conversation for the chat model
    conversation = [
        {"role": "system", "content": knowledge_base},
        {"role": "user", "content": question}
    ]

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0,  # the lower the temperature, the less creative the output
        max_tokens=1000  # maximum number of tokens
    )

    # Extract the answer
    answer = response['choices'][0]['message']['content']

    # Append assistant's answer to conversation history
    st.session_state['conversation_history'] += 'AI客服: ' + answer + '\n'

    # Display the conversation history
    st.text_area("聊天历史", st.session_state['conversation_history'], height=1000)
