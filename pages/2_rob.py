# import json, pandas as pd, streamlit as st

# st.title("Reorder Buffer Viewer")

# def load_trace(path):
#     with open(path) as f:
#         return [json.loads(line) for line in f]

# trace = load_trace("dump_files/rob_trace.json")
# cycle = st.session_state.get("cycle", 0)
# cycle = min(cycle, len(trace)-1)

# st.write(f"Current Cycle: {cycle}")
# df = pd.DataFrame(trace[cycle]["ROB"])
# st.dataframe(df, use_container_width=True)

import json, pandas as pd, streamlit as st

st.title("Reorder Buffer Viewer")

if "page_cycle_rob" not in st.session_state:
    st.session_state["page_cycle_rob"] = 0

sync = st.checkbox("🔗 Sync with Global", value=True)

if sync:
    cycle = st.session_state["global_cycle"]
else:
    cycle = st.session_state["page_cycle_rob"]

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅ Prev (ROB)"):
        st.session_state["page_cycle_rob"] = max(cycle - 1, 0)
with col2:
    st.metric("ROB Cycle", cycle)
with col3:
    if st.button("➡ Next (ROB)"):
        st.session_state["page_cycle_rob"] = cycle + 1

def load_trace(path):
    with open(path) as f:
        return [json.loads(line) for line in f]
trace = load_trace("dump_files/rob_trace.json")

cycle = min(cycle, len(trace)-1)
st.write(f"顯示第 {cycle} 個 cycle 狀態")
df = pd.DataFrame(trace[cycle]["ROB"])
st.dataframe(df, use_container_width=True)
