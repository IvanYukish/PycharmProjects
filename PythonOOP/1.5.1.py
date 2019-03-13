class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capalicy = capacity

    def can_add(self, v):
        if self.capalicy >= v + self.count:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(self.count):
            self.count += v
