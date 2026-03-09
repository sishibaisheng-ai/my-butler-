import streamlit as st
import dashscope
from http import HTTPStatus

st.set_page_config(page_title="Qwen Butler", page_icon="🏮")
st.title("🏮 通义千问·私人管家")

with st.sidebar:
    st.header("密钥配置")
    api_key = st.text_input("请输入阿里云 API Key:", type="password")

thought = st.text_area("把脑子里的乱麻写下来...", height=150)

if st.button("🚀 请求千问梳理"):
    if not api_key:
        st.error("请先在左侧输入 API Key！")
    elif not thought:
        st.warning("内容为空哦。")
    else:
        with st.spinner("千问（多模态版）正在深度思考中..."):
            dashscope.api_key = api_key
            # 使用多模态接口调用 Qwen3.5-Plus
            response = dashscope.MultiModalConversation.call(
                model="qwen3.5-plus",
                messages=[{
                    "role": "user",
                    "content": [{"text": f"你是一个私人深度思考管家。请帮我梳理逻辑并给3条建议：\n\n{thought}"}]
                }]
            )
            
            if response.status_code == HTTPStatus.OK:
                st.subheader("💡 梳理结果：")
                # 多模态接口返回内容的取值方式略有不同
                st.write(response.output.choices[0].message.content[0]["text"])
            else:
                st.error(f"出错啦：{response.message}")
