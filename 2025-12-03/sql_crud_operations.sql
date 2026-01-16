-- Creation of Database
CREATE DATABASE college_db;
USE college_db;

-- Creation of Table
CREATE TABLE students (
student_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(30),
last_name VARCHAR(50),
email VARCHAR(100),
age INT,
city VARCHAR(50)
);

-- Inserting Values
INSERT INTO students (first_name, last_name, email, age, city) 
VALUES
('Bob', 'John', 'bob@gmail.com', 22, 'Kochi'),
('Eze', 'Boi', 'eze@gmail.com', 24, 'Kolkata');

SELECT * FROM students;

-- Selecting Specific Data
SELECT first_name,last_name
FROM students
WHERE city = "Kolkata"

-- Ordering By Age
SELECT first_name,last_name
FROM students
ORDER BY age DESC

-- Updating City
UPDATE students
SET city = "Banglore"
WHERE student_id = 2;

-- Updating Lastname
UPDATE students
SET city = "Arteta"
WHERE email = "eze@gmail.com";

-- DELETE A RECORD
DELETE FROM students
WHERE student_id = 2;

-- DELETE A RECORD
DELETE FROM students
WHERE city = "DELHI";

-- Deleting Table including Schema
DROP TABLE students

-- Deleting DATABASE
DROP DATABASE college_db
