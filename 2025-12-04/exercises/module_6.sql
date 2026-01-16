--MODULE 6: MySQL CRUD & Joins (Full Backend) (11 Exercises)


--40. Create a database retail_app and two tables: customers and orders. Insert 10 rows.
CREATE DATABASE retail_app;

USE retail_app;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (name, customer_id, last_name, email, phone, city) VALUES
('John', 1, 'john.doe@example.com', '9876543210', 'Coimbatore'),
('Jane', 2, 'jane.smith@example.com', '9876543211', 'Chennai'),
('Raj', 3, 'raj.kumar@example.com', '9876543212', 'Bangalore'),
('Priya', 4, 'priya.sharma@example.com', '9876543213', 'Delhi'),
('Arun', 5, 'arun.nair@example.com', '9876543214', 'Mumbai'),
('Meera', 6, 'meera.patel@example.com', '9876543215', 'Pune'),
('Suresh', 7, 'suresh.reddy@example.com', '9876543216', 'Hyderabad'),
('Anita', 8, 'anita.verma@example.com', '9876543217', 'Kolkata'),
('Vikram', 9, 'vikram.singh@example.com', '9876543218', 'Jaipur'),
('Neha', 10, 'neha.gupta@example.com', '9876543219', 'Lucknow');

INSERT INTO orders (customer_id, order_date, amount, status) VALUES
(1, '2025-12-01', 2500.00, 'Completed'),
(2, '2025-12-02', 1800.50, 'Pending'),
(3, '2025-12-03', 3200.75, 'Completed'),
(4, '2025-12-04', 1500.00, 'Cancelled'),
(5, '2025-12-05', 2750.25, 'Completed'),
(6, '2025-12-06', 1999.99, 'Pending'),
(7, '2025-12-06', 4500.00, 'Completed'),
(8, '2025-12-06', 800.00, 'Completed'),
(9, '2025-12-06', 1200.00, 'Pending'),
(10, '2025-12-06', 600.00, 'Completed');

SELECT * FROM customers
SELECT * FROM orders


--41. Write SOL: fetch all customers who placed more than 2 orders.
SELECT *
FROM customers
INNER JOIN orders
ON customer.customer_id = orders.customer_id
WHERE


--42. Write SOL:
--list products that were never ordered.
--43. Write SOL:
--total amount spent by each customer.
--44. Write SOL: orders of each customer including customers with zero orders (left join).
--all products and match orders even if no sale occurred (right join).
--45. Write SOL:
--46. Write SQL
--: find customers ordering from multiple categories.
--47. Write SOL: list top 3 highest revenue orders.
--48. Write SOL:
--detect missing customer-id or product-id in orders.
--generate a report of (customer x month x total amount).
--49. Write SOL:
--50. Write a SQL query using CROSS JOIN to generate all (customer x product) combinations.