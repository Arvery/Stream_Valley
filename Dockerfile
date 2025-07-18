# 使用官方 Streamlit 镜像作为基础（推荐）
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 拷贝项目文件
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量，避免 Streamlit 弹出提示或监听 localhost
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_ENABLEXSRFFILTER=false

# 启动 streamlit
CMD ["streamlit", "run", "Home.py"]
