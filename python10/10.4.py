class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):             # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):             # nigdy nie jest pusta
        return False

    def put(self, data):
        self.items.append(data)

    def get(self):
        return self.items.pop(0)   # mało wydajne!