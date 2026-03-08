import streamlit as st

# 1. 显示包含名字的标题
st.title("HELLO，I am [LI ZHANGBIN]")

# 2. 显示子标题“关于我”
# 使用 subheader 可以让页面结构更清晰
st.header("about me")

# 3. 使用 st.text() 显示关于你的 3 个事实
st.text("1. i am lover Developer.")
st.text("2. I really like writing automation tools with Python。")
st.text("3. I am learning how to build interactive web applications through Streamlit。")

# 4. 显示成功消息
st.success("welcome to streamlit")