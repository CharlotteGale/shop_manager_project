DROP TABLE IF EXISTS items_orders;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    unit_price DECIMAL(10, 2),
    quantity INT
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    order_date DATE
);

CREATE TABLE items_orders (
    item_id int,
    order_id int,
    CONSTRAINT fk_item FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE,
    CONSTRAINT fk_order FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
    PRIMARY KEY (item_id, order_id)
);

INSERT INTO items (name, unit_price, quantity) VALUES
('Laptop', 899.99, 15),
('Wireless Mouse', 24.99, 50),
('USB-C Cable', 12.99, 100),
('Mechanical Keyboard', 129.99, 25),
('Headphones', 79.99, 40);

INSERT INTO orders (customer_name, order_date) VALUES
('Alice Johnson', '2024-12-15'),
('Bob Smith', '2024-12-16'),
('Carol Williams', '2024-12-17'),
('David Brown', '2024-12-18'),
('Alice Johnson', '2024-12-19');

INSERT INTO items_orders (item_id, order_id) VALUES
(1, 1),  -- Alice ordered a Laptop
(3, 1),  -- Alice also ordered a USB-C Cable
(2, 2),  -- Bob ordered a Wireless Mouse
(4, 3),  -- Carol ordered a Mechanical Keyboard
(5, 4),  -- David ordered Headphones
(2, 5),  -- Alice ordered a Wireless Mouse
(3, 5);  -- Alice also ordered a USB-C Cable