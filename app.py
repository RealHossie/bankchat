# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
import streamlit as st
import openai

# 读取 .env 参数
load_dotenv()

# 获取 OPENAI_API_KEY
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 配置 OpenAI key
openai.api_key = OPENAI_API_KEY

# Streamlit
st.title('AI客服机器人')

knowledge_base = st.text_area("请输入你的知识库:")

question = st.text_input("请输入你的问题:")

if st.button('提交'):
    # 定义会话
    conversation = [
        {"role": "system", "content": knowledge_base},
        {"role": "user", "content": question}
    ]

    # 调取 OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0,  # 数值越高创造性越强
        max_tokens=1000  # 最大token数量
    )

    # 获取答案
    answer = response['choices'][0]['message']['content']

    st.write('AI客服:', answer)
