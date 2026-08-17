INSERT INTO Customers (name, email, city, registered_at)
VALUES
('Artem', 'artem@example.com', 'Kaunas', '2024-01-01'),
('John Doe', 'john@example.com', 'Vilnius', '2024-02-10'),
('Maria Smith', 'maria@example.com', 'Riga', '2024-03-05');

INSERT INTO Orders (customer_id, order_date)
VALUES
(1, '2024-04-01'),
(1, '2024-04-15'),
(2, '2024-04-20'),
(3, '2024-05-01');

INSERT INTO OrderItems (order_id, product, price, quantity)
VALUES
(1, 'Laptop', 900, 1),
(1, 'Mouse', 25, 2),
(2, 'Keyboard', 45, 1),
(3, 'Phone', 600, 1),
(4, 'Shirt', 30, 3);
