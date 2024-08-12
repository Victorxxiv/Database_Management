-- Create a new -- Drop a table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10, 2)
);

-- Insert records
INSERT INTO employees (first_name, last_name, salary)
VALUES ('John', 'Doe', 50000),
('Jane', 'Smith', 60000),
('Alice', 'Johnson', 70000);

-- Read data
SELECT * FROM employees WHERE salary > 55000;

-- Update data
UPDATE employees
SET salary = 75000
WHERE first_name = 'Jane';

-- Delete data
DELETE FROM employees WHERE last_name = 'Doe';