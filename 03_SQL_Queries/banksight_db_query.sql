--- VERIFY DATA (IMPORTANT)
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM transactions;
SELECT COUNT(*) FROM support_tickets;

--- 🔹 1️⃣ CUSTOMER & ACCOUNT ANALYSIS
--- Q1: How many customers exist per city, and what is their average account balance?
SELECT 
    c.city,
    COUNT(DISTINCT c.customer_id) AS total_customers,
    ROUND(AVG(a.account_balance), 2) AS avg_balance
FROM customers c
JOIN accounts a 
    ON c.customer_id = a.customer_id
GROUP BY c.city
ORDER BY total_customers DESC;

--- Q2: Which account type (Savings, Current, Loan, etc.) holds the highest total balance?
SELECT 
    c.account_type,
    ROUND(SUM(a.account_balance), 2) AS total_balance
FROM customers c
JOIN accounts a
    ON c.customer_id = a.customer_id
GROUP BY c.account_type
ORDER BY total_balance DESC;

--- Q3: Who are the top 10 customers by total account balance across all account types?
SELECT 
    c.customer_id,
    c.name,
    a.account_balance
FROM customers c
JOIN accounts a 
    ON c.customer_id = a.customer_id
ORDER BY a.account_balance DESC
LIMIT 10;

--- Q4: Which customers opened accounts in 2023 with a balance above ₹1,00,000?
SELECT 
    c.customer_id,
    c.name,
    a.account_balance
FROM customers c
JOIN accounts a 
    ON c.customer_id = a.customer_id
WHERE EXTRACT(YEAR FROM c.join_date) = 2023
  AND a.account_balance > 100000;

 --- 🔹 2️⃣ TRANSACTION BEHAVIOR
 --- Q5: What is the total transaction volume (sum of amounts) by transaction type?
SELECT 
    txn_type,
    ROUND(SUM(amount), 2) AS total_amount
FROM transactions
GROUP BY txn_type
ORDER BY total_amount DESC;

--- Q6: How many failed transactions occurred for each transaction type?
SELECT 
    txn_type,
    COUNT(*) AS failed_txns
FROM transactions
WHERE status = 'failed'
GROUP BY txn_type;

--- Q7: What is the total number of transactions per transaction type?
SELECT 
    txn_type,
    COUNT(*) AS total_txns
FROM transactions
GROUP BY txn_type;

--- Q8: Which accounts have 5 or more high-value transactions above ₹20,000?
SELECT 
    customer_id,
    COUNT(*) AS high_value_txns
FROM transactions
WHERE amount > 20000
GROUP BY customer_id
HAVING COUNT(*) >= 5;

--- 🔹 3️⃣ LOAN INSIGHTS
--- Q9: What is the average loan amount and interest rate by loan type (Personal, Auto, Home, etc.)?
SELECT 
    loan_type,
    ROUND(AVG(loan_amount), 2) AS avg_loan,
    ROUND(AVG(interest_rate), 2) AS avg_interest
FROM loans
GROUP BY loan_type;

--- Q10: Which customers currently hold more than one active or approved loan?
SELECT 
    customer_id,
    COUNT(*) AS active_loans
FROM loans
WHERE loan_status IN ('Active', 'Approved')
GROUP BY customer_id
HAVING COUNT(*) > 1;

--- Q11: Who are the top 5 customers with the highest outstanding (non-closed) loan amounts?
SELECT 
    customer_id,
    SUM(loan_amount) AS total_outstanding
FROM loans
WHERE loan_status != 'Closed'
GROUP BY customer_id
ORDER BY total_outstanding DESC
LIMIT 5;

--- 🔹 4️⃣ BRANCH & DEMOGRAPHICS
--- Q12: What is the average loan amount per branch?
SELECT 
    branch,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount
FROM loans
GROUP BY branch;

--- Q13: How many customers exist in each age group (e.g., 18–25, 26–35, etc.)?
SELECT 
    CASE
        WHEN age BETWEEN 18 AND 25 THEN '18-25'
        WHEN age BETWEEN 26 AND 35 THEN '26-35'
        WHEN age BETWEEN 36 AND 50 THEN '36-50'
        ELSE '50+'
    END AS age_group,
    COUNT(*) AS total_customers
FROM customers
GROUP BY age_group;

--- 🔹 5️⃣ SUPPORT TICKETS & EXPERIENCE
--- Q14: Which issue categories have the longest average resolution time?
SELECT 
    issue_category,
    ROUND(AVG(resolution_days), 2) AS avg_resolution_days
FROM support_tickets
WHERE resolution_days IS NOT NULL
GROUP BY issue_category
ORDER BY avg_resolution_days DESC;

--- Q15: Which support agents have resolved the most critical tickets with high customer ratings (≥4)?
SELECT 
    support_agent,
    COUNT(*) AS tickets_resolved
FROM support_tickets
WHERE priority = 'Critical'
  AND customer_rating >= 4
GROUP BY support_agent
ORDER BY tickets_resolved DESC;

-----------------------------------------------------------------------------------------------------------------------
------------------------------ COMPLETED ------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------














