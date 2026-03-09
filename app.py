import streamlit as st
import dashscope
from http import HTTPStatus

# 设置页面
st.set_page_config(page_title="Qwen Butler", page_icon="🏮")
st.title("🏮 通义千问·私人管家")

# 在侧边栏设置 API Key
with st.sidebar:
    api_key = st.text_input("请输入阿里云 DashScope API Key:", type="password")
    st.info("从阿里云百炼控制台获取钥匙")

# 灵感记录区
thought = st.text_area("把脑子里的乱麻写下来...", height=150)

if st.button("🚀 请求千问梳理"):
    if not api_key:
        st.error("请先在左侧输入 API Key！")
    elif not thought:
        st.warning("内容为空，千问没法思考哦。")
    else:
        with st.spinner("千问正在深度思考中..."):
            dashscope.api_key = api_key
            response = dashscope.Generation.call(
                model=dashscope.Generation.Models.qwen_turbo,
                prompt=f"你是一个私人深度思考管家。请帮我梳理以下想法的逻辑，并给出3条启发性建议：\n\n{thought}"
            )
            
            if response.status_code == HTTPStatus.OK:
                st.success("【千问梳理完成】")
                st.write(response.output.text)
            else:
                st.error(f"出错啦：{response.message}")
