from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.item import Item
from lib.order_repository import OrderRepository
from lib.order import Order
from datetime import datetime

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager.sql")

    def run(self):
        print("Welcome to the shop management program!")
        print(" ")
        print("What do you want to do?")
        print(" 1 - List all shop items")
        print(" 2 - Create a new item")
        print(" 3 - List all orders")
        print(" 4 - Create a new order")
        print(" ")
        choice = int(input("Enter 1, 2, 3, or 4"))

        if choice == 1:
            item_repository = ItemRepository(self._connection)
            items = item_repository.list_items()

            for item in items:
                print("Here is a list of all shop items: ")
                print(f" #{item.id} {item.name} - Unit price: £{item.unit_price} - Quantity: {item.quantity}")

        elif choice == 2:
            item_repository = ItemRepository(self._connection)

            name = input("Enter item name: ")
            unit_price = float(input("Enter unit price: "))
            quantity = int(input("Enter quantity: "))

            new_item = Item(0, name, unit_price, quantity)
            
            item_repository.create_new_item(new_item)

            print(f"Successfully added {name} to the inventory!")

        elif choice == 3:
            order_repository = OrderRepository(self._connection)
            orders = order_repository.list_orders()

            for order in orders:
                print("Here is a list of all orders: ")
                print(f" #{order.id} - Customer Name: {order.customer_name} - Ordered On: {order.order_date}")

        elif choice == 4:
            order_repository = OrderRepository(self._connection)

            customer_name = input("Enter customer's name: ")

            order_date = datetime.now().date()

            new_order = Order(0, customer_name, order_date)
            
            order_repository.create_new_order(new_order)

            print(f"Successfully placed new order for {customer_name}!")


if __name__ == '__main__':
    app = Application()
    app.run()