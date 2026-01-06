import streamlit as st
from db import engine
import pandas as pd

st.title("✏️ CRUD Operations – Customers")

# READ
st.subheader("📖 View Customers")
df = pd.read_sql("SELECT * FROM customers", engine)
st.dataframe(df)

# CREATE
st.subheader("➕ Add Customer")
cid = st.text_input("Customer ID")
name = st.text_input("Name")
gender = st.selectbox("Gender", ["M", "F"])
age = st.number_input("Age", min_value=18)
city = st.text_input("City")
account_type = st.selectbox("Account Type", ["Savings", "Current"])
join_date = st.date_input("Join Date")

if st.button("Insert Customer"):
    engine.execute(
        f"""
        INSERT INTO customers
        VALUES ('{cid}','{name}','{gender}',{age},
                '{city}','{account_type}','{join_date}')
        """
    )
    st.success("Customer inserted successfully")

# DELETE
st.subheader("❌ Delete Customer")
del_id = st.text_input("Customer ID to delete")

if st.button("Delete Customer"):
    engine.execute(
        f"DELETE FROM customers WHERE customer_id='{del_id}'"
    )
    st.warning("Customer deleted")
