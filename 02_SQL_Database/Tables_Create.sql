--- CREATE CUSTOMERS TABLE
CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    name TEXT,
    gender CHAR(1),
    age INT,
    city TEXT,
    account_type TEXT,
    join_date DATE
);

--- CREATE ACCOUNTS TABLE
CREATE TABLE accounts (
    customer_id VARCHAR(10),
    account_balance NUMERIC(12,2),
    last_updated TIMESTAMP
);

--- CREATE TRANSACTIONS TABLE
CREATE TABLE transactions (
    txn_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(10),
    txn_type TEXT,
    amount NUMERIC(12,2),
    txn_time TIMESTAMP,
    status TEXT
);

--- CREATE LOANS TABLE (STANDALONE)
CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    customer_id INT,
    account_id INT,
    branch TEXT,
    loan_type TEXT,
    loan_amount INT,
    interest_rate NUMERIC(5,2),
    loan_term_months INT,
    start_date DATE,
    end_date DATE,
    loan_status TEXT
);

--- CREATE CREDIT_CARD TABLE
CREATE TABLE credit_cards (
    card_id INT PRIMARY KEY,
    customer_id INT,
    account_id INT,
    branch TEXT,
    card_number TEXT,
    card_type TEXT,
    card_network TEXT,
    credit_limit INT,
    current_balance NUMERIC(12,2),
    issued_date DATE,
    expiry_date DATE,
    status TEXT
);

--- CREATE BRANCHES TABLE
CREATE TABLE branches (
    branch_id INT PRIMARY KEY,
    branch_name TEXT,
    city TEXT,
    manager_name TEXT,
    total_employees INT,
    branch_revenue NUMERIC(15,2),
    opening_date DATE,
    performance_rating INT
);

--- CREATE SUPPORT_TICKETS TABLE
CREATE TABLE support_tickets (
    ticket_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    account_id VARCHAR(10),
    loan_id INT,
    branch_name TEXT,
    issue_category TEXT,
    description TEXT,
    date_opened DATE,
    date_closed DATE,
    priority TEXT,
    status TEXT,
    resolution_remarks TEXT,
    support_agent TEXT,
    channel TEXT,
    customer_rating INT,
    resolution_days INT
);







