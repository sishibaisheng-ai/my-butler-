import streamlit as st
import random

# Personal Butler App
st.set_page_config(page_title="My Butler", page_icon="🧠")
st.title("🧠 私人思考管家")

if st.button("✨ 获取启发提问"):
    prompts = ["你现在在逃避什么？", "这件事最本质的逻辑是什么？", "一年后看，这还重要吗？"]
    st.info(random.choice(prompts))

thought = st.text_area("记录你的碎片想法...")
if st.button("保存并梳理"):
    st.success("已记录，准备接入 AI 分析...")
