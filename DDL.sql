CREATE DATABASE CompanyDB;
USE CompanyDB;

CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    salary INT
);


INSERT INTO Employees VALUES (1, 'Arjun', 'Sales', 50000);
INSERT INTO Employees VALUES (2, 'Meena', 'HR', 45000);
INSERT INTO Employees VALUES (3, 'Ravi', 'IT', 60000);


UPDATE Employees
SET salary = 55000
WHERE id = 1;

DELETE FROM Employees
WHERE id = 2;

-- 
SELECT * FROM Employees;