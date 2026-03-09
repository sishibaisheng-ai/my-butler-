import streamlit as st
import dashscope
from http import HTTPStatus

# 1. 页面基本设置
st.set_page_config(page_title="Qwen Butler", page_icon="🏮")
st.title("🏮 通义千问·私人管家")

# 2. 在侧边栏设置 API Key
with st.sidebar:
    st.header("密钥配置")
    api_key = st.text_input("请输入阿里云 API Key:", type="password")
    st.info("从阿里云百炼控制台获取 sk- 开头的钥匙")

# 3. 主界面：灵感记录区
thought = st.text_area("把脑子里的乱麻写下来...", height=150)

# 4. 核心逻辑：点击按钮请求 AI
if st.button("🚀 请求千问梳理"):
    if not api_key:
        st.error("请先在左侧输入 API Key！")
    elif not thought:
        st.warning("内容为空，千问没法思考哦。")
    else:
        with st.spinner("千问正在深度思考中..."):
            # 设置你拿到的那串 sk- 钥匙
            dashscope.api_key = api_key
            
            # 正确调用 Qwen3.5-Plus 模型
            response = dashscope.Generation.call(
                model="qwen3.5-plus",
                prompt=f"你是一个私人深度思考管家。请帮我梳理逻辑并给3条建议：\n\n{thought}"
            )
            
            # 检查结果并显示
            if response.status_code == HTTPStatus.OK:
                st.subheader("💡 梳理结果：")
                st.write(response.output.text)
            else:
                st.error(f"出错啦：{response.message}")
                st.info("提示：请确认你已在百炼后台‘立即开通’了 Qwen3.5-Plus 模型。")
