class BMW:
    def fuel_type(self):
        print('Premium')
    def max_speed(self):
        print('191 mph')
class Ferrari:
    def fuel_type(self):
        print('High Octane')
    def max_speed(self):
        print('218 mph')
b = BMW()
f = Ferrari()
cars = (b,f)
for i in cars:
    i.fuel_type()
    i.max_speed()
