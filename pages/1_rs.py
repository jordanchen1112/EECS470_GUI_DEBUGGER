# import json, pandas as pd, streamlit as st

# st.title("Reservation Station Viewer")

# def load_trace(path):
#     with open(path) as f:
#         return [json.loads(line) for line in f]

# trace = load_trace("dump_files/rs_trace.json")
# cycle = st.session_state.get("cycle", 0)

# # 確保 cycle 不超出範圍
# cycle = min(cycle, len(trace)-1)

# st.write(f"Current Cycle: {cycle}")
# df = pd.DataFrame(trace[cycle]["RS"])
# st.dataframe(df, use_container_width=True)

import json, pandas as pd, streamlit as st

st.title("Reservation Station Viewer")

# 初始化頁面 cycle
if "page_cycle_rs" not in st.session_state:
    st.session_state["page_cycle_rs"] = 0

# 是否跟隨全域 cycle
sync = st.checkbox("🔗 Sync with Global", value=True)

# 若同步 → 使用全域 cycle
if sync:
    cycle = st.session_state["global_cycle"]
else:
    cycle = st.session_state["page_cycle_rs"]

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅ Prev (RS)"):
        st.session_state["page_cycle_rs"] = max(cycle - 1, 0)
with col2:
    st.metric("RS Cycle", cycle)
with col3:
    if st.button("➡ Next (RS)"):
        st.session_state["page_cycle_rs"] = cycle + 1

# 載入 trace
def load_trace(path):
    with open(path) as f:
        return [json.loads(line) for line in f]
trace = load_trace("dump_files/rs_trace.json")

cycle = min(cycle, len(trace)-1)
st.write(f"顯示第 {cycle} 個 cycle 狀態")
df = pd.DataFrame(trace[cycle]["RS"])
st.dataframe(df, use_container_width=True)
