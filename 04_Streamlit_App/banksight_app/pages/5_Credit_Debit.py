import streamlit as st
import pandas as pd
from db import engine

st.title("💰 Credit / Debit Simulation (Banking Logic)")

# -------------------------
# Input: Customer ID
# -------------------------
customer_id = st.text_input("Enter Customer ID")

if customer_id:

    # Fetch current balance
    query = f"""
        SELECT account_balance
        FROM accounts
        WHERE customer_id = '{customer_id}'
    """
    df = pd.read_sql(query, engine)

    if df.empty:
        st.error("❌ Account not found")
    else:
        current_balance = df["account_balance"].iloc[0]
        st.success(f"💼 Current Balance: ₹ {current_balance}")

        amount = st.number_input(
            "Enter Amount",
            min_value=0,
            step=100
        )

        col1, col2 = st.columns(2)

        # -------------------------
        # DEPOSIT
        # -------------------------
        with col1:
            if st.button("➕ Deposit"):
                engine.execute(
                    f"""
                    UPDATE accounts
                    SET account_balance = account_balance + {amount}
                    WHERE customer_id = '{customer_id}'
                    """
                )
                st.success("✅ Amount Deposited Successfully")
                st.info("Balance updated in database")

        # -------------------------
        # WITHDRAW
        # -------------------------
        with col2:
            if st.button("➖ Withdraw"):
                if current_balance - amount < 1000:
                    st.error("❌ Minimum balance ₹1000 must be maintained")
                else:
                    engine.execute(
                        f"""
                        UPDATE accounts
                        SET account_balance = account_balance - {amount}
                        WHERE customer_id = '{customer_id}'
                        """
                    )
                    st.success("✅ Amount Withdrawn Successfully")
                    st.info("Balance updated in database")
