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

# global list to hold the conversation history
conversation = [{"role": "system", "content": knowledge_base}]

if st.button('提交'):
    # Append user's question to conversation
    conversation.append({"role": "user", "content": question})

    # If there are more than 3 exchanges (6 messages), only keep the most recent ones
    if len(conversation) > 6:
        conversation = conversation[-6:]

    # Call the OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0,  # the lower the temperature, the less creative the output
        max_tokens=1000  # maximum number of tokens
    )

    # Extract the answer
    answer = response['choices'][0]['message']['content']

    # Append assistant's answer to conversation
    conversation.append({"role": "assistant", "content": answer})

    st.write('AI客服:', answer)
