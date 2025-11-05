import streamlit as st

st.set_page_config(page_title="EECS470 GUI Debugger", layout="wide")

# 初始化 session_state
if "cycle" not in st.session_state:
    st.session_state["cycle"] = 0

st.title("EECS470 CPU GUI Debugger")

# Sidebar 控制所有頁面共用的 cycle
cycle = st.slider("Global Cycle", 0, 100, st.session_state["cycle"])
st.session_state["cycle"] = cycle

st.markdown("從左側選單切換模組（RS / ROB / ...），所有頁面會同步到相同 cycle。")
