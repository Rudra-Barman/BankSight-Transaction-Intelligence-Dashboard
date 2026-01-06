import streamlit as st
import pandas as pd
from db import engine

st.title("📊 View Tables")

table = st.selectbox(
    "Select Dataset",
    [
        "customers",
        "accounts",
        "transactions",
        "loans",
        "credit_cards",
        "branches",
        "support_tickets"
    ]
)

df = pd.read_sql(f"SELECT * FROM {table}", engine)
st.dataframe(df, use_container_width=True)
