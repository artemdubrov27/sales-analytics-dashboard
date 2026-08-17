-- 1. Загальний дохід
SELECT SUM(price * quantity) AS TotalRevenue
FROM OrderItems;

-- 2. Дохід по клієнтах
SELECT c.name, SUM(oi.price * oi.quantity) AS Revenue
FROM Customers c
JOIN Orders o ON c.id = o.customer_id
JOIN OrderItems oi ON o.id = oi.order_id
GROUP BY c.id
ORDER BY Revenue DESC;

-- 3. Топ-продукти
SELECT product, SUM(price * quantity) AS Revenue
FROM OrderItems
GROUP BY product
ORDER BY Revenue DESC;

-- 4. Середній чек
SELECT AVG(order_total) AS AverageOrderValue
FROM (
    SELECT o.id, SUM(oi.price * oi.quantity) AS order_total
    FROM Orders o
    JOIN OrderItems oi ON o.id = oi.order_id
    GROUP BY o.id
);

-- 5. Замовлення по місяцях
SELECT substr(order_date, 1, 7) AS Month, COUNT(*) AS OrdersCount
FROM Orders
GROUP BY Month;
