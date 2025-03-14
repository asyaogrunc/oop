class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart

    def process_order(self):
        print(f"{self.customer.name} has placed an order for the following items:")
        self.cart.view_cart()
