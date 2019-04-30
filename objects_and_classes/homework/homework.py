"""
<<<<<<< HEAD
Вам небхідно написати 3 класи. Мільйонери Гаражі та Автомобілі.
Звязкок наступний один мільйонер може мати багато гаражів.
=======
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
>>>>>>> 6c5d86d12b48c9fae0a46a2d7133a611235b4671
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""
<<<<<<< HEAD
from typing import List
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from uuid import uuid4


class Car:

    def __init__(self, producer, type, price: float, mileage: float):
        if producer not in CARS_PRODUCER or type not in CARS_TYPES:
            print("Please, enter valid values <producer> and <type>")
        else:
            self.producer = producer
            self.type = type
            self.price = float(price)
            self.mileage = float(mileage)
            self.number = uuid4().hex

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __str__(self):
        return f"{self.producer} / {self.type}, Price:{self.price}, Mileage:{self.mileage}, Number:{self.number}"

    def replace_number(self):
        self.number = uuid4().hex











class Garage:

    cars: List[Car]


    def __init__(self, town, places, cars=None, owner=None):
        if town not in TOWNS:     # перевірка параметру <town>
            print("Please, enter valid values <town>")
        else:
            self.town = town
            self.cars = cars if cars is not None else []
            self.places = places
            self.owner = owner

    def __str__(self):
        return f"{self.town}, {self.places}, {self.cars}, {self.owner}"

    def add(self, car: Car):   # додавання машини в гараж
        if self.places <= len(self.cars):
            print("Sorry, no room for a new car")
        else:
            self.cars.append([str(car)])

    def remove(self, car_number):  # віднімання машини з гаражу; машина ідентифікується по унікальному номеру
        for car in self.cars:
            for number in car:
                if car_number in number:
                    self.cars.remove(car)




    def hit_hat(self):    # сумарна вартість машин в гаражі
        return sum(map(lambda car: car.price, self.cars))



first = Garage('London', 5)
delcar = Car('Ford', 'Sedan', 11111, 111)
first.add(delcar)
first.add(Car('Ford', 'Sedan', 22222, 222))
first.add(Car('Ford', 'Sedan', 33333, 333))

print('add - ', first)
first.remove(delcar.number)
print('remove - ', first)

print(first.hit_hat())



























#
# class Millionaire:
#
#     def __init__(self, name, garages=[], register_id=uuid.uuid4()):
#         self.name = str(name)
#         self.register_id = register_id.hex
#         self.garages = garages
#
#     def garages_count(self):
#         return len(self.garages)
#
#     def cars_count(self):
#         return len([car for garage in self.garages for car in garage])
#
#     def add_garage(self, garage: Garage):
#         self.garages.append(garage)
#
#     def empty_garage(self):
#         return
#     def add_car(self, garage: Garage):
#         if garage














=======


class Cesar:
    pass


class Car:
    pass


class Garage:
    pass
>>>>>>> 6c5d86d12b48c9fae0a46a2d7133a611235b4671
