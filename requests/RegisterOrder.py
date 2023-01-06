class Order:
    def __init__(self, customer_id):
        self.customer_id = customer_id


class OrderItem:
    def __init__(self, order_id, quantity, product_id):
        self.order_id = order_id
        self.quantity = quantity
        self.product_id = product_id
