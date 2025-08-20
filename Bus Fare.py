class Bus:
    def __init__(self,capacity):
        self.capacity = capacity
class Fare(Bus):
    def __init__(self,capacity):
        super().__init__(capacity)
    def price(self):
        print('Price in £:', self.capacity/5)
bus = Fare(100)
bus.price()