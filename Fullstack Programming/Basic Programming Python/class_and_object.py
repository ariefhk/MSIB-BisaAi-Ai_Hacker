class Car:
    carCount = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Car.carCount += 1

    def getCar(self):
        return f'Name: {self.name}, Color: {self.color}'


ford = Car('Ford', 'Merah')
toyota = Car('Toyota', 'Hijau')
print(f'Total Mobil: {int(Car.carCount)}')
print(f'Mobil 1 \n{ford.getCar()}')
print(f'Mobil 2 \n{toyota.getCar()}')
