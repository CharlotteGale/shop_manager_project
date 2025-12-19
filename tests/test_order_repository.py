from lib.order_repository import OrderRepository
from lib.order import Order
from datetime import date

"""
When we call OrderRepository#list_orders
We get a list of Order objects reflecting seed data
"""
def test_get_all_order_records(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = OrderRepository(db_connection)

    orders = repo.list_orders()

    assert len(orders) == 5
    assert orders == [
        Order(1, 'Alice Johnson', date(2024, 12, 15)),
        Order(2, 'Bob Smith', date(2024, 12, 16)),
        Order(3, 'Carol Williams', date(2024, 12, 17)),
        Order(4, 'David Brown', date(2024, 12, 18)),
        Order(5, 'Alice Johnson', date(2024, 12, 19))
    ]

"""
When we call OrderRepository#find_by_order_id
We get a single Order object reflecting the seed data
Filtered by order_id
"""
def test_get_single_order_record_by_id(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = OrderRepository(db_connection)

    order = repo.find_by_order_id(3)

    assert order == Order(3, 'Carol Williams', date(2024, 12, 17))

"""
When we call OrderRepository#create_new_order
We add a new Order obeject to the seed data
"""
def test_creates_new_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = OrderRepository(db_connection)

    repo.create_new_order(Order(None, 'Kris Kringle', '2024-12-24'))

    assert len(repo.list_orders()) == 6

    order = repo.find_by_order_id(6)
    
    assert order == Order(6, 'Kris Kringle', date(2024, 12, 24))