class Car:
    def __init__(self, brand, model, year, mileage, engine_type, engine_fuel, engine_power, engine_size):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine = Engine(engine_type, engine_fuel, engine_power, engine_size)
    def __str__(self):
        return f'{self.brand} {self.model} {self.year} года выпуска, пробег {self.mileage}\n Параметры двигателя: {self.engine}'

class Garage:
    def __init__(self):
        self.cars = []
    def add_to_garage(self, car: Car):
        self.cars.append(car)
    def __str__(self):
        line = "Машины в гараже: \n"
        for car in self.cars:
            line += f'{car}\n'
        return line


class Engine:
    def __init__(self, type, fuel, power, size):
        self.type = type
        self.fuel = fuel
        self.power = power
        self.size = size
    def __str__(self):
        return f' Двигатель {self.type}, {self.fuel} , мощность - {self.power}, объём - {self.size}'

class Owner:
    def __init__(self, name, dob, cars=None):
        self.name = name
        self.dob = dob
        self.cars = []
    def __str__(self):
        answer = ''
        for car in self.cars:
            answer += f'{car.brand} {car.model}'
        return f'{self.name}, {self.dob}, купил {answer}'
    def buy_car(self, car):
        self.cars.append(car)
        return f'{car.brand} {car.model} куплена'
class ServiceStation:
    def __init__(self, cars):
        self.cars = cars
        price = 0
    def checkup(self):
        for car in self.cars.cars:
            if car.mileage > 20000:
                return f'Пробег {car.brand} {car.model} слишком большой'
    def price(self):
        price = 100_000
        price_for_each = []
        for car in self.cars.cars:
            if car.mileage <= 20000:
                price += 200_000
            if int(car.year) > 2005:
                price += 200_000
            price_for_each.append(price)

        return f'Цена авто: {price_for_each}'

    def __str__(self):
        n = 1
        for car in self.cars:
            n += 1
            print(f'Машина №{n}: {car}')

car1 = Car('Lada', 'Granta', '2000', 15000, '4-цилиндровый', 'бензин', 90, 1.6)
car2 = Car('Toyota', 'Camry', '2017', 25000, 'V6', 'бензин', 250, 3.5)
car3 = Car('Toyota', 'Camry', '2000', 35000, 'V6', 'бензин', 250, 3.5)

Car_garage = Garage()

Car_garage.add_to_garage(car1)
Car_garage.add_to_garage(car2)
Car_garage.add_to_garage(car3)

print(Car_garage)

person1 = Owner('Иван Иванов', '12.12.2000')
service1 = ServiceStation(Car_garage)

print(person1.buy_car(car1))

print(service1.price())

def by_model(garage: Garage):
    st = input('Введите модель: ')
    answer = []
    for car in garage.cars:
        if car.model == st:
            answer.append(f'Машина: {car.mileage}, {car.year}')
    return answer
print(by_model(Car_garage))




