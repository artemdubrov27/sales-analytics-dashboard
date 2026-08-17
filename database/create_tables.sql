DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS OrderItems;

CREATE TABLE Customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    city TEXT,
    registered_at TEXT
);

CREATE TABLE Orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES Customers(id)
);

CREATE TABLE OrderItems (
    id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product TEXT,
    price REAL,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES Orders(id)
);
