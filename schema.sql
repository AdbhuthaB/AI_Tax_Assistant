CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE tax_records (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    income DECIMAL(10,2) NOT NULL,
    expenses DECIMAL(10,2) NOT NULL,
    deductions TEXT
);