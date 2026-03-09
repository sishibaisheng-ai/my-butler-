进口 streamlit as圣
import random

st.set_page_config(page_title="私人思考管家", page_icon="🧠")

st.title("🧠 私人思考管家")
st.write("你好！我是你的深度思考伴侣。")

# 模块 1：思维闪击
with st.container():
    if st.button("✨ 抽一张思维启发卡"):
        prompts = [
            "如果你现在的精力只有 10%，你会如何处理这件事？",
            "这件事的‘第一性原理’（最本质的逻辑）是什么？",
            "你是在解决问题，还是在缓解焦虑？",
            "如果一年后回头看，这件事还值得你纠结吗？"
        ]
        st.info(random.choice(prompts))

# 模块 2：乱麻梳理
st.divider()
thought = st.text_area("把此刻脑子里的乱麻、灵感、不爽都写下来：", height=200)

if st.button("🚀 开始梳理逻辑"):
    if thought:
        st.success("【管家初步分析】")
        st.write(f"收到。你刚才记录了约 {len(thought)} 字的内容。")
        st.write("接下来我们将通过 Gemini AI 接口进行深度重构。")
    else:
        st.warning("主人，请先输入你的想法。")
