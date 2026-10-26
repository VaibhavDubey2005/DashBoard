
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #071426, #102d50, #164e63);
    color: white;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #0a192c;
}

h1, h2, h3, p, label {
    color: #f1f5f9 !important;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
}

[data-testid="stDataFrame"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
}

div[data-baseweb="select"] > div {
    background-color: #16324f;
    color: white;
    border-radius: 8px;
}

hr {
    border-color: rgba(255,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Customer Analytics Dashboard")
st.caption("CUSTOMER INSIGHTS  |  DATA OVERVIEW")

try:
    df = pd.read_csv("powerbi_table_schema.csv")

    total_tables = df["Table"].nunique()
    total_columns = len(df)

    c1, c2, c3 = st.columns(3)

    c1.metric("📁 Total Tables", total_tables)
    c2.metric("📋 Total Columns", total_columns)
    c3.metric("✅ Status", "Ready")

    st.divider()

    st.subheader("🔎 Explore Your Data")

    selected_table = st.selectbox(
        "Select a table",
        df["Table"].unique()
    )

    filtered = df[df["Table"] == selected_table]

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("🗂️ Complete Table Structure")
    st.dataframe(df, use_container_width=True, hide_index=True)

except FileNotFoundError:
    st.error(
        "CSV file nahi mili. "
        "powerbi_table_schema.csv ko app.py ke same folder mein rakho."
    )
