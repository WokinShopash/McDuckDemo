
class Order:
    def __init__(self, id, bigmacs=0, cola=0, fries=0):
        self.bigmacs = bigmacs
        self.cola = cola
        self.fries = fries
        self.id = id
        self.status = 'queue'


class OrderStorage:
    POSSIBLE_ITEMS = ['bigmacs', 'cola', 'fries', ]

    def __init__(self):
        self.orders = []
        self.queue_start = 0

    def create_order(self, bigmacs=0, cola=0, fries=0):
        new_id = len(self.orders)

        self.orders.append(
            Order(new_id, bigmacs, cola, fries)
        )
        return new_id

    def get_status(self, id):
        return self.orders[id].status

    def finish(self, id):
        order = self.orders[id]
        assert order.status == 'cooking'
        order.status = 'ready'

    def get_next_order(self):
        if len(self.orders) <= self.queue_start:
            return -1
        order = self.orders[self.queue_start]
        assert order.status == 'queue'
        order.status = 'cooking'
        self.queue_start += 1
        return order.id
