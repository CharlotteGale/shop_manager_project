from lib.order import Order

"""
Order constructs with an id, customer_name, and order_date
"""
def test_order_constructs():
    order = Order(1, 'Alice Johnson', '2024-12-15')

    assert order.id == 1
    assert order.customer_name == 'Alice Johnson'
    assert order.order_date == '2024-12-15'

"""
We can compare two identical orders
And have them be equal
"""
def test_orders_are_equal():
    order1 = Order(1, 'Alice Johnson', '2024-12-15')
    order2 = Order(1, 'Alice Johnson', '2024-12-15')

    assert order1 == order2

"""
We can format order strings nicely
"""
def test_orders_format_nicely():
    order = Order(1, 'Alice Johnson', '2024-12-15')

    assert str(order) == "Order(1, Alice Johnson, 2024-12-15)"