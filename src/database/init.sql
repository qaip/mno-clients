CREATE TABLE clients (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  account_number VARCHAR(20) UNIQUE NOT NULL,
  address VARCHAR(100) NOT NULL,
  mobile_phone VARCHAR(20) UNIQUE,
  landline VARCHAR(20) UNIQUE
);
