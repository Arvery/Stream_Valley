import streamlit as st
import os
from pathlib import Path
import random
import base64

# ----------------------
# 页面配置
# ----------------------
st.set_page_config(page_title="📚 笔记浏览", layout="wide")


# ----------------------
# 函数：读取图片并转 base64
# ----------------------
def get_img_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# ----------------------
# 函数：设置背景图与透明遮罩
# ----------------------
def set_background_and_overlay(png_path, opacity=0.6):
    base64_str = get_img_base64(png_path)
    css = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{base64_str}") no-repeat center center fixed;
        background-size: cover;
    }}
    .overlay-layer {{
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(255,255,255,{opacity});
        z-index: 0;
    }}
    </style>
    <div class="overlay-layer"></div>
    """
    st.markdown(css, unsafe_allow_html=True)


# ----------------------
# 设置背景图
# ----------------------
set_background_and_overlay("assets/ground.png", opacity=0.85)


# ----------------------
# 音乐播放器设置
# ----------------------
music_files = {
    "Stardew Valley Overture": "assets/01 - Stardew Valley Overture.mp3",
    "Cloud Country": "assets/02 - Cloud Country.mp3",
    "Grandpa's Theme": "assets/03 - Grandpa's Theme.mp3"
}
music_options = ["请选择一首音乐"] + list(music_files.keys())
music_choice = st.sidebar.selectbox("🎵 选择背景音乐", music_options)


# ----------------------
# Markdown 文件选择器
# ----------------------
notes_dir = "notes"
md_files = [f for f in os.listdir(notes_dir) if f.endswith(".md")]
note_options = ["请选择一篇笔记"] + sorted(md_files, reverse=True)
selected_file = st.sidebar.selectbox("📝 选择笔记", note_options)


# ----------------------
# 侧边栏：比赛介绍信息
# ----------------------
with st.sidebar:
    st.title("🏆 比赛介绍")
    st.markdown("""
### 📌 2025腾讯开悟人工智能全球公开赛  
**第七届全国高校计算机能力挑战赛 · 智能交通信号灯调度赛道**

本赛道由腾讯开悟平台与成都交投智慧交通科技集团有限公司联合定制，聚焦城市交通出行需求，参赛团队需设计基于强化学习等算法的**交通信号灯调度策略**，以实现智能化信号调度目标。
""")
    st.markdown("🔗 [点击查看比赛详情](https://aiarena.tencent.com/aiarena/zh/match/open-competition-2025/open-competition-2025-5)")


# ----------------------
# 主体区域：播放音乐
# ----------------------
if music_choice != "请选择一首音乐":
    st.title("📚 每日 Markdown 笔记")
    st.markdown(f"### ▶️ 当前选择音乐：**{music_choice}**")
    st.info("🎵 请点击下面的播放器按钮手动播放音乐")

    music_path = Path(music_files[music_choice])
    if music_path.exists():
        with open(music_path, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
    else:
        st.error(f"❌ 音频文件未找到：{music_path}")


# ----------------------
# 主体区域：展示 Markdown 笔记
# ----------------------
if selected_file != "请选择一篇笔记":
    with open(os.path.join(notes_dir, selected_file), "r", encoding="utf-8") as f:
        content = f.read()

    st.markdown(f"---\n### 📄 当前笔记：`{selected_file}`")
    st.markdown(content, unsafe_allow_html=True)

    # ---- 文末盲盒按钮 ----
    st.markdown("---")
    st.markdown("### 🎁 到达文末，试试你的好运，点一下盲盒吧！")

    if st.button("✨ 点击开启盲盒"):
        effect = random.choice(["balloons", "snow", "toast"])

        if effect == "balloons":
            st.balloons()
            st.success("🎈 直冲云霄 节节高")
        elif effect == "snow":
            st.snow()
            st.info("❄️ 冬天来了，春天还会远吗？")
        elif effect == "toast":
            try:
                st.toast("🎉 恭喜你抽中了神秘祝福！积累生命里的小确信吧！", icon="🍀")
            except AttributeError:
                st.warning("🔔 恭喜你抽中了神秘祝福，积累生命里的小确信吧！")

