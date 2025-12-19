from lib.item_repository import ItemRepository
from lib.item import Item

"""
When we call ItemRepository#list_items
We get a list of Item objects reflecting seed data
"""
def test_get_all_item_records(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ItemRepository(db_connection)

    items = repo.list_items()

    assert len(items) == 5
    assert items == [
        Item(1, 'Laptop', 899.99, 15),
        Item(2, 'Wireless Mouse', 24.99, 50),
        Item(3, 'USB-C Cable', 12.99, 100),
        Item(4, 'Mechanical Keyboard', 129.99, 25),
        Item(5, 'Headphones', 79.99, 40)
    ]

"""
When we call ItemRepository#find_by_item_id
We get a single Item object reflecting the seed data
Filtered by item_id
"""
def test_get_single_item_record_by_id(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ItemRepository(db_connection)

    item = repo.find_by_item_id(1)

    assert item == Item(1, 'Laptop', 899.99, 15)

"""
When we call ItemRepository#create_new_item
We add a new Item obeject to the seed data
"""
def test_creates_new_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ItemRepository(db_connection)

    repo.create_new_item(Item(None, 'Desk Mat XL', 19.99, 100))

    assert len(repo.list_items()) == 6

    item = repo.find_by_item_id(6)
    
    assert item == Item(6, 'Desk Mat XL', 19.99, 100)