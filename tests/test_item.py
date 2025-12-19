from lib.item import Item

"""
Item constructs with an id, name, unit_price, and quantity
"""
def test_item_constructs():
    item = Item(1, 'Laptop', 899.99, 15)

    assert item.id == 1
    assert item.name == 'Laptop'
    assert item.unit_price == 899.99
    assert item.quantity == 15

"""
We can compare two identical items
And have them be equal
"""
def test_items_are_equal():
    item1 = Item(1, 'Laptop', 899.99, 15)
    item2 = Item(1, 'Laptop', 899.99, 15)

    assert item1 == item2

"""
We can format Item strings nicely
"""
def test_items_format_nicely():
    item = Item(1, 'Laptop', 899.99, 15)

    assert str(item) == "Item(1, Laptop, 899.99, 15)"