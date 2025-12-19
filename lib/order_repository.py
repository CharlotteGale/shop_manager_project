from lib.order import Order
from datetime import date

class OrderRepository:
    def __init__(self, connection):
        self._connection = connection

    def list_orders(self):
        rows = self._connection.execute(
            'SELECT * FROM orders'
        )
        orders = []
        for row in rows:
            order = Order(row['id'], row['customer_name'], row['order_date'])
            orders.append(order)
        return orders
    
    def find_by_order_id(self, order_id):
        rows = self._connection.execute(
            'SELECT * FROM orders WHERE id = %s',
            [order_id]
        )

        row = rows[0]
        return Order(row['id'], row['customer_name'], row['order_date'])
    
    def create_new_order(self, new_order):
        self._connection.execute(
            'INSERT INTO orders (customer_name, order_date) ' \
                'VALUES ( %s, %s)',
                [new_order.customer_name, new_order.order_date]
        )