-- Create the restaurant database
CREATE DATABASE restaurant_db;
USE restaurant_db;

-- Create the menu_items table
CREATE TABLE menu_items (
    menu_item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category ENUM('Starters', 'Main Course', 'Desserts', 'Beverages') NOT NULL,
    cost_price DECIMAL(10, 2) NOT NULL,
    selling_price DECIMAL(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE
);

-- Create the inventory table
CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category ENUM('Vegetables', 'Spices', 'Grains', 'Beverages') NOT NULL,
    stock_quantity INT NOT NULL,
    reorder_level INT NOT NULL,
    unit ENUM('kg', 'liters', 'units') NOT NULL,
    supplier_id INT NOT NULL,
    last_order_date DATE,
    next_reorder_date DATE
);

-- Create the suppliers table
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(50),
    item_supplied VARCHAR(100),
    payment_due DECIMAL(10, 2) DEFAULT 0.00
);

-- Create the sales table
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE NOT NULL,
    sale_time TIME NOT NULL,
    order_id INT NOT NULL,
    menu_item_id INT NOT NULL,
    quantity INT NOT NULL,
    price_per_unit DECIMAL(10, 2) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    payment_method ENUM('Cash', 'Card', 'Online') NOT NULL,
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(menu_item_id)
);

-- Create the employees table
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role ENUM('Chef', 'Waiter', 'Cashier', 'Manager') NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    hire_date DATE NOT NULL,
    hours_worked DECIMAL(5, 2) DEFAULT 0.00,
    leave_balance INT DEFAULT 0
);

-- Create the expenses table
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    category ENUM('Rent', 'Utilities', 'Marketing', 'Maintenance') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    description VARCHAR(255)
);

-- Create the customer_feedback table
CREATE TABLE customer_feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    feedback_date DATE NOT NULL,
    customer_name VARCHAR(100),
    menu_item_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comments TEXT,
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(menu_item_id)
);

-- Insert sample data into menu_items
INSERT INTO menu_items (name, category, cost_price, selling_price)
VALUES 
('Masala Dosa', 'Main Course', 30.00, 80.00),
('Idli Sambar', 'Starters', 20.00, 50.00),
('Medu Vada', 'Starters', 15.00, 45.00),
('Rava Kesari', 'Desserts', 25.00, 60.00),
('Filter Coffee', 'Beverages', 10.00, 30.00);

-- Insert sample data into inventory
INSERT INTO inventory (item_name, category, stock_quantity, reorder_level, unit, supplier_id, last_order_date, next_reorder_date)
VALUES 
('Rice', 'Grains', 200, 50, 'kg', 1, '2024-10-01', '2024-10-20'),
('Dal', 'Grains', 100, 30, 'kg', 2, '2024-10-05', '2024-10-25'),
('Coconut Oil', 'Spices', 50, 10, 'liters', 3, '2024-10-03', '2024-10-18'),
('Spices Mix', 'Spices', 30, 10, 'kg', 1, '2024-10-02', '2024-10-17'),
('Coffee Beans', 'Beverages', 20, 5, 'kg', 2, '2024-10-06', '2024-10-21');

-- Insert sample data into suppliers
INSERT INTO suppliers (name, contact, item_supplied, payment_due)
VALUES 
('Food Suppliers Co.', '123-456-7890', 'Rice, Dal', 15000.00),
('Spice World', '098-765-4321', 'Spices, Coffee Beans', 8000.00),
('Oils & Grains Ltd', '234-567-8901', 'Coconut Oil', 5000.00);

-- Insert sample data into sales
INSERT INTO sales (sale_date, sale_time, order_id, menu_item_id, quantity, price_per_unit, total, payment_method)
VALUES 
('2024-10-15', '12:30:00', 101, 1, 2, 80.00, 160.00, 'Card'),
('2024-10-15', '13:00:00', 102, 2, 3, 50.00, 150.00, 'Cash'),
('2024-10-16', '10:30:00', 103, 5, 1, 30.00, 30.00, 'Online'),
('2024-10-16', '15:15:00', 104, 3, 4, 45.00, 180.00, 'Card'),
('2024-10-17', '18:45:00', 105, 4, 1, 60.00, 60.00, 'Cash');

-- Insert sample data into employees
INSERT INTO employees (name, role, salary, hire_date, hours_worked, leave_balance)
VALUES 
('Suresh Kumar', 'Chef', 30000.00, '2022-01-15', 160.00, 10),
('Ravi Shankar', 'Waiter', 15000.00, '2023-02-20', 120.00, 5),
('Meena Sharma', 'Cashier', 18000.00, '2023-05-10', 130.00, 7),
('Vijay Singh', 'Manager', 35000.00, '2021-11-10', 180.00, 15);

-- Insert sample data into expenses
INSERT INTO expenses (expense_date, category, amount, description)
VALUES 
('2024-10-10', 'Rent', 50000.00, 'Monthly restaurant rent'),
('2024-10-12', 'Utilities', 8000.00, 'Electricity and water bills'),
('2024-10-14', 'Marketing', 5000.00, 'Social media ads for October'),
('2024-10-16', 'Maintenance', 3000.00, 'Equipment maintenance');

-- Insert sample data into customer_feedback
INSERT INTO customer_feedback (feedback_date, customer_name, menu_item_id, rating, comments)
VALUES 
('2024-10-15', 'Rajesh', 1, 5, 'The masala dosa was fantastic!'),
('2024-10-15', 'Anita', 2, 4, 'The idli was good, but could be softer.'),
('2024-10-16', 'Ramesh', 3, 5, 'Best Medu Vada I have had in a while!'),
('2024-10-16', 'Priya', 5, 3, 'The coffee was okay, not strong enough for my taste.');

