CREATE DATABASE emp;
USE emp;

CREATE TABLE employee_details(
	emp_id INT PRIMARY KEY,
    emp_name VARCHAR(20),
    salary INT,
    dept_name VARCHAR(20)
);

INSERT INTO employee_details VALUES
(1001, "Alen", 30000, "Tax"),
(1002, "Bob", 45000, "Consulting"),
(1003, "Candice", 40000, "Finance"),
(1004, "Diana", 40000, "HR");

SELECT * FROM employee_details;