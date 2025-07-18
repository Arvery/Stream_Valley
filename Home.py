# Streamlit Stream Valley 主页展示
# 作者：QAQ
# 功能：展示背景音乐选择、个人信息卡片、Markdown文稿、图文轮播、珠子故事简介等

import streamlit as st
import os
import base64
from pathlib import Path
import streamlit.components.v1 as components
import markdown

# 页面设置
st.set_page_config(page_title="stream valley", page_icon="🌟", layout="wide")

# 获取图片 base64 编码
def get_img_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ---- 首部 banner 背景图展示 ----
img_base64 = get_img_base64("assets/bank.png")

st.markdown(
    f"""
    <style>
    .banner {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        height: 500px;
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    </style>
    <div class="banner"></div>
    """,
    unsafe_allow_html=True
)

# ---- 音乐选择 ----
music_files = {
    "Stardew Valley Overture": "01 - Stardew Valley Overture.mp3",
    "Cloud Country": "02 - Cloud Country.mp3",
    "Grandpa's Theme": "03 - Grandpa's Theme.mp3"
}

music_choice = st.sidebar.selectbox("🎵 选择背景音乐", list(music_files.keys()))
music_path = f"assets/{music_files[music_choice]}"

if os.path.exists(music_path):
    with open(music_path, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
else:
    st.warning("音乐文件未找到！")

# ---- 侧边栏个人信息 ----
with st.sidebar:
    st.title("👤 个人信息")
    st.image("assets/self2.png", width=200)
    st.write("姓名：QAQ")
    st.write("职业：农民👨‍🌾")
    st.write("📧 邮箱：3434014515@qq.com")
    st.write("📍 城市：stream valley")
    st.markdown("[🔗 GitHub](https://github.com/Arvery)")

# ---- 主体欢迎语 ----
if "visited" not in st.session_state:
    st.session_state.visited = True
    st.balloons()

st.markdown("""
<h1 style='text-align: center; font-size: 48px; font-family: "Segoe UI", sans-serif; color: #4B0082;'>
欢迎来到 Stream Valley 👋
</h1>
""", unsafe_allow_html=True)

# ---- 显示 Markdown 文本内容 ----
md_path = Path("stream.md")
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

md_html = markdown.markdown(md_content)
img_base64_1 = get_img_base64("assets/cloud.png")

# ---- 添加透明遮罩和 markdown 内容框 ----
components.html(f"""
<html>
<head>
<style>
body {{
    margin: 0;
    padding: 0;
    background-image: url("data:image/png;base64,{img_base64_1}");
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-position: center;
    height: 100vh;
}}
.overlay {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(255,255,255,0.6);
    z-index: 0;
}}
.content-box {{
    position: relative;
    z-index: 1;
    width: 90vw;
    height: 80vh;
    margin: 5vh auto;
    background: rgba(255, 255, 255, 0.5);
    border-radius: 10px;
    padding: 20px;
    overflow-y: auto;
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
    font-family: sans-serif;
}}
</style>
</head>
<body>
    <div class="overlay"></div>
    <div class="content-box">
        {md_html}
    </div>
</body>
</html>
""", height=800, scrolling=False)

# ---- 首饰展示滑稽 ----
def img_to_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def show_carousel(image_folder="assets/gallery"):
    image_paths = sorted(Path(image_folder).glob("*.png")) + sorted(Path(image_folder).glob("*.jpg"))
    slides = ""
    for img in image_paths:
        encoded = img_to_base64(img)
        slides += f'''
        <div class="swiper-slide" style="display: flex; justify-content: center; align-items: center;">
            <img src="data:image/png;base64,{encoded}" 
                 style="max-width: 100%; max-height: 500px; object-fit: contain; border-radius: 10px;" />
        </div>
        '''

    html_code = f"""
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css"/>
    <style>
    .swiper-container {{
        width: 100%;
        height: 520px;
        background-color: #f8f8f8;
    }}
    </style>
    <div class="swiper-container">
        <div class="swiper-wrapper">
            {slides}
        </div>
        <div class="swiper-pagination"></div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
    </div>
    <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
    <script>
    const swiper = new Swiper('.swiper-container', {{
        loop: true,
        pagination: {{ el: '.swiper-pagination', clickable: true }},
        navigation: {{ nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' }},
    }});
    </script>
    """
    st.components.v1.html(html_code, height=550, scrolling=False)

# 调用图片滑稽
st.header("📸 我的首饰小铺")
show_carousel()

# ---- 中间文案经典名话 ----
st.markdown("""
<div style='text-align: center; font-size: 18px;'>

<h3>🌛 每个人心中都有一个童话 ✨</h3>

<p style='color: #d62728; font-weight: bold;'>
“每个人心中都有一个童话，只是有的人忘记了。”
</p>

<p>
如果可以把 🌈<strong>梦想</strong> 与 ✨<strong>童话</strong> 戴在手上、放在心上，<br>
🌟 <strong>生命便有了形状与支柱</strong>，
</p>

<p>
🚪走到哪里，也不会忘记自己的方向。
</p>

<hr style='border-top: 1px dashed #aaa;'>

<p>
🏱 <strong>敬请期待吧！</strong><br>
每一颗 ✨珠子✨，都有属于 ❤️ta 的故事！
</p>

</div>
""", unsafe_allow_html=True)
