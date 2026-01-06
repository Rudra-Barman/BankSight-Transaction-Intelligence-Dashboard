import streamlit as st
import pandas as pd
from db import engine

st.title("🔍 Filter Data")

# Step 1: Select table
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

# Step 2: Load data
df = pd.read_sql(f"SELECT * FROM {table}", engine)

# Step 3: Column selection
column = st.selectbox("Select Column to Filter", df.columns)

# Step 4: Value selection
value = st.text_input("Enter value")

# Step 5: Apply filter
if value:
    filtered_df = df[df[column].astype(str).str.contains(value, case=False)]
else:
    filtered_df = df

st.dataframe(filtered_df, use_container_width=True)
