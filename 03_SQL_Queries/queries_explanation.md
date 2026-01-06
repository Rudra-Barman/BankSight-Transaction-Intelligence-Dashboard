# SQL Queries Explanation – BankSight Transaction Intelligence Dashboard

This document provides a brief explanation and business relevance of each SQL query used in the project.

---

## 1️⃣ Customer & Account Analysis

### Q1. City-wise customers and average account balance
Purpose:
Identifies the number of customers in each city along with their average account balance.

Business Insight:
Helps the bank understand high-value cities and regional customer distribution for targeted marketing.

---

### Q2. Account type with the highest total balance
Purpose:
Calculates the total balance held under each account type.

Business Insight:
Shows which account products contribute the most to overall bank deposits.

---

### Q3. Top 10 customers by account balance
Purpose:
Fetches the top 10 customers with the highest account balances.

Business Insight:
Identifies high-net-worth customers for personalized services and retention strategies.

---

### Q4. Customers joined in 2023 with balance above ₹1,00,000
Purpose:
Filters customers who joined in 2023 and maintain a high account balance.

Business Insight:
Highlights newly acquired high-value customers.

---

## 2️⃣ Transaction Behavior Analysis

### Q5. Total transaction amount by transaction type
Purpose:
Summarizes total transaction amounts for each transaction type (credit/debit).

Business Insight:
Provides insights into overall cash inflow and outflow patterns.

---

### Q6. Failed transactions count by transaction type
Purpose:
Counts failed transactions grouped by transaction type.

Business Insight:
Helps identify operational issues and areas requiring system improvements.

---

### Q7. Total number of transactions by type
Purpose:
Counts the total number of transactions by transaction type.

Business Insight:
Analyzes customer transaction behavior and preferred transaction modes.

---

### Q8. Customers with 5 or more high-value transactions
Purpose:
Identifies customers who have performed at least five transactions above ₹20,000.

Business Insight:
Acts as a potential fraud detection indicator and helps monitor suspicious activity.

---

## 3️⃣ Loan Insights

### Q9. Average loan amount and interest rate by loan type
Purpose:
Calculates average loan amount and interest rate for each loan category.

Business Insight:
Helps assess loan portfolio performance and pricing strategies.

---

### Q10. Customers with multiple active or approved loans
Purpose:
Finds customers holding more than one active or approved loan.

Business Insight:
Assists in credit risk analysis and exposure management.

---

### Q11. Top 5 customers with highest outstanding loan amount
Purpose:
Identifies customers with the highest total outstanding loan amounts.

Business Insight:
Supports loan recovery prioritization and risk monitoring.

---

## 4️⃣ Branch & Demographic Analysis

### Q12. Average loan amount per branch
Purpose:
Calculates average loan amounts issued by each branch.

Business Insight:
Compares branch-level loan performance.

---

### Q13. Customer distribution by age group
Purpose:
Groups customers into age categories and counts them.

Business Insight:
Helps understand demographic patterns and tailor banking products accordingly.

---

## 5️⃣ Support Tickets & Customer Experience

### Q14. Issue categories with longest average resolution time
Purpose:
Calculates average resolution time for each support issue category.

Business Insight:
Identifies bottlenecks in customer support operations.

---

### Q15. Support agents resolving the most critical tickets with high ratings
Purpose:
Counts critical tickets resolved by support agents with customer ratings ≥ 4.

Business Insight:
Highlights high-performing support agents and service quality.
