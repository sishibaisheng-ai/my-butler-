import streamlit as st
import dashscope
from http import HTTPStatus

# 1. 页面基础配置
st.set_page_config(page_title="Qwen Butler", page_icon="🏮", layout="centered")
st.title("🏮 通义千问·私人管家")

# 2. 侧边栏：密钥自动化管理
with st.sidebar:
    st.header("密钥配置")
    # 尝试从 Secrets 自动获取钥匙，如果没有则默认为空
    default_key = st.secrets.get("DASHSCOPE_API_KEY", "")
    
    api_key = st.text_input(
        "请输入阿里云 API Key:", 
        value=default_key, 
        type="password",
        help="从阿里云百炼控制台获取 sk- 开头的钥匙"
    )
    
    if default_key:
        st.success("✅ 已从后台自动加载密钥")
    else:
        st.info("💡 提示：在 Secrets 后台配置后可免输入")

# 3. 主界面：灵感记录区
thought = st.text_area("把脑子里的乱麻写下来...", height=150, placeholder="例如：我想策划一次团建，但是预算有限...")

# 4. 核心逻辑：调用 Qwen3.5-Plus
if st.button("🚀 请求千问梳理"):
    if not api_key:
        st.error("请先在左侧输入 API Key！")
    elif not thought:
        st.warning("内容为空，千问没法思考哦。")
    else:
        with st.spinner("千问正在深度逻辑梳理中..."):
            # 设置 API Key
            dashscope.api_key = api_key
            
            # 使用 MultiModalConversation 接口（适配 Qwen3.5-Plus）
            response = dashscope.MultiModalConversation.call(
                model="qwen3.5-plus",
                messages=[{
                    "role": "user",
                    "content": [{"text": f"你是一个私人深度思考管家。请帮我梳理逻辑并给3条建议：\n\n{thought}"}]
                }]
            )
            
            # 5. 结果处理与显示
            if response.status_code == HTTPStatus.OK:
                st.subheader("💡 梳理结果：")
                # 提取多模态接口返回的文本内容
                answer = response.output.choices[0].message.content[0]["text"]
                st.markdown(answer)
            else:
                st.error(f"调用失败！错误信息：{response.message}")
                st.info("提示：请确认你的 API Key 是否正确，且后台已开通 Qwen3.5-Plus 模型。")
