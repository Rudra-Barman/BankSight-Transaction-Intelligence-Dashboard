# BankSight – User Guide

## Overview
BankSight is an interactive Streamlit-based banking analytics dashboard.
It allows users to explore banking data, perform CRUD operations, and
analyze transactions and loan insights.

---

## Application Features
- View customer, account, transaction, loan, and support ticket tables
- Filter data using multiple conditions
- Perform Create, Read, Update, and Delete (CRUD) operations
- Simulate credit and debit transactions
- Analyze banking insights and potential fraud signals

---

## Navigation Guide
- **Introduction**: Project overview
- **View Tables**: View raw database tables
- **Filter Data**: Apply column-level filters
- **CRUD Operations**: Manage records
- **Credit/Debit**: Transaction simulation
- **Analytical Insights**: Business insights
- **About Creator**: Developer profile

---

## How to Run the Application
1. Ensure Python 3.9+ is installed
2. Install required libraries:
```bash
pip install pandas sqlalchemy psycopg2 streamlit
```
3. Navigate to the Streamlit app directory:
```bash
cd banksight_app
```
4. Run the application:
```bash
streamlit run app.py
```

---

## Notes
- Ensure PostgreSQL database credentials are correctly configured
- The application uses a relational database backend
