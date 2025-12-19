from lib.item import Item

class ItemRepository:
    def __init__(self, connection):
        self._connection = connection

    def list_items(self):
        rows = self._connection.execute(
            'SELECT * FROM items'
        )
        items = []
        for row in rows:
            item = Item(row['id'], row['name'], float(row['unit_price']), row['quantity'])
            items.append(item)
        return items
    
    def find_by_item_id(self, item_id):
        rows = self._connection.execute(
            'SELECT * FROM items WHERE id = %s',
            [item_id]
        )

        row = rows[0]
        return Item(row['id'], row['name'], float(row['unit_price']), row['quantity'])
    
    def create_new_item(self, new_item):
        self._connection.execute(
            'INSERT INTO items (name, unit_price, quantity) ' \
                'VALUES (%s, %s, %s)',
                [new_item.name, new_item.unit_price, new_item.quantity]
        )