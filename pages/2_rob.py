import json, pandas as pd, streamlit as st

st.title("Reorder Buffer Viewer")

def load_trace(path):
    with open(path) as f:
        return [json.loads(line) for line in f]

trace = load_trace("dump_files/rob_trace.json")
cycle = st.session_state.get("cycle", 0)
cycle = min(cycle, len(trace)-1)

st.write(f"Current Cycle: {cycle}")
df = pd.DataFrame(trace[cycle]["ROB"])
st.dataframe(df, use_container_width=True)
