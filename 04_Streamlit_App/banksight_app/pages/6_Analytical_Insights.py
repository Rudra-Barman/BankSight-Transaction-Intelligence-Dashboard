import streamlit as st
import pandas as pd
from db import engine

st.title("🧠 Analytical Insights")

# ===============================
# 15+ SQL Queries (FULL LIST)
# ===============================
query_map = {

    # 1️⃣ CUSTOMER & ACCOUNT ANALYSIS
    "Q1 Customers by City": """
        SELECT city, COUNT(*) AS total_customers
        FROM customers
        GROUP BY city
    """,

    "Q2 Account Type vs Total Balance": """
        SELECT c.account_type, SUM(a.account_balance) AS total_balance
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
        GROUP BY c.account_type
    """,

    "Q3 Top 10 Customers by Balance": """
        SELECT c.customer_id, c.name, a.account_balance
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
        ORDER BY a.account_balance DESC
        LIMIT 10
    """,

    "Q4 High Balance Customers Joined in 2023": """
        SELECT c.customer_id, c.name, a.account_balance
        FROM customers c
        JOIN accounts a ON c.customer_id = a.customer_id
        WHERE EXTRACT(YEAR FROM c.join_date) = 2023
          AND a.account_balance > 100000
    """,

    # 2️⃣ TRANSACTION BEHAVIOR
    "Q5 Transaction Amount by Type": """
        SELECT txn_type, SUM(amount) AS total_amount
        FROM transactions
        GROUP BY txn_type
    """,

    "Q6 Failed Transactions by Type": """
        SELECT txn_type, COUNT(*) AS failed_txns
        FROM transactions
        WHERE status = 'failed'
        GROUP BY txn_type
    """,

    "Q7 Transaction Count by Type": """
        SELECT txn_type, COUNT(*) AS total_txns
        FROM transactions
        GROUP BY txn_type
    """,

    "Q8 High Value Transactions (Fraud Indicator)": """
        SELECT customer_id, COUNT(*) AS high_value_txns
        FROM transactions
        WHERE amount > 20000
        GROUP BY customer_id
        HAVING COUNT(*) >= 5
    """,

    # 3️⃣ LOAN INSIGHTS
    "Q9 Avg Loan & Interest by Type": """
        SELECT loan_type,
               AVG(loan_amount) AS avg_loan,
               AVG(interest_rate) AS avg_interest
        FROM loans
        GROUP BY loan_type
    """,

    "Q10 Customers with Multiple Active Loans": """
        SELECT customer_id, COUNT(*) AS active_loans
        FROM loans
        WHERE loan_status IN ('Active','Approved')
        GROUP BY customer_id
        HAVING COUNT(*) > 1
    """,

    "Q11 Top 5 Customers with Highest Outstanding Loans": """
        SELECT customer_id, SUM(loan_amount) AS total_outstanding
        FROM loans
        WHERE loan_status <> 'Closed'
        GROUP BY customer_id
        ORDER BY total_outstanding DESC
        LIMIT 5
    """,

    # 4️⃣ BRANCH & DEMOGRAPHICS
    "Q12 Avg Loan Amount per Branch": """
        SELECT branch, AVG(loan_amount) AS avg_loan_amount
        FROM loans
        GROUP BY branch
    """,

    "Q13 Customers by Age Group": """
        SELECT
        CASE
            WHEN age BETWEEN 18 AND 25 THEN '18-25'
            WHEN age BETWEEN 26 AND 35 THEN '26-35'
            WHEN age BETWEEN 36 AND 50 THEN '36-50'
            ELSE '50+'
        END AS age_group,
        COUNT(*) AS total_customers
        FROM customers
        GROUP BY age_group
    """,

    # 5️⃣ SUPPORT & EXPERIENCE
    "Q14 Avg Resolution Time by Issue Category": """
        SELECT issue_category, AVG(resolution_days) AS avg_days
        FROM support_tickets
        WHERE resolution_days IS NOT NULL
        GROUP BY issue_category
        ORDER BY avg_days DESC
    """,

    "Q15 Best Support Agents (Critical & Rating ≥4)": """
        SELECT support_agent, COUNT(*) AS tickets_resolved
        FROM support_tickets
        WHERE priority = 'Critical'
          AND customer_rating >= 4
        GROUP BY support_agent
        ORDER BY tickets_resolved DESC
    """
}

# ===============================
# UI PART
# ===============================
st.success(f"Total Analytical Queries Implemented: {len(query_map)}")

choice = st.selectbox("Select Business Question", list(query_map.keys()))
query = query_map[choice]

st.code(query)   # SQL transparency
df = pd.read_sql(query, engine)

st.dataframe(df, use_container_width=True)

# Chart (only if 2 columns)
if df.shape[1] == 2:
    st.bar_chart(df.set_index(df.columns[0]))
