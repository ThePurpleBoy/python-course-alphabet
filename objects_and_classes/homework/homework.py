
"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.
Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.
    Автомобілі можна порівнювати між собою за ціною.
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
    garages_count() - вертає кількість гаражів.
    сars_count() - вертає кількість машин.
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.
    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""
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
        return f"{self.producer} - {self.type}, Price:{self.price}, Mileage:{self.mileage}, Number:{self.number}"

    def __repr__(self):
        return f"< {self.producer} / {self.type} / {self.price} / {self.mileage} / {self.number} >"

    def replace_number(self):
        self.number = uuid4().hex





class Garage:

    cars: List[Car]

    def __init__(self, town, places: int, cars=None, owner=None):
        if town not in TOWNS:
            print("Please, enter valid values <town>")
        else:
            self.town = town
            self.cars = cars if cars is not None else []
            self.places = places
            self.owner = owner
            self.current = 0
            self.free_places = self.places - len(self.cars)

    def __str__(self):
        return f"{self.town}, {self.places}, {self.cars}, {self.owner}"

    def __repr__(self):
        return f"< {self.town}, {self.places}, {self.cars} >"

    def add(self, car: Car):
        if self.places <= len(self.cars):
            print("Sorry, no room for a new car")
        else:
            self.cars.append(car)

    def remove(self, car: Car):
        self.cars.remove(car)

    def hit_hat(self):
        return sum(map(lambda car: car.price, self.cars))





class Cesar:
    garages = List[Garage]

    def __init__(self, name: str, garages=None):
        self.name = name
        self.garages = garages if garages is not None else []
        self.register_id = uuid4().hex

    def __str__(self):
        return f'{self.name}: {self.garages}'

    def __repr__(self):
        return f'{self.name}/ {self.garages}'

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __ne__(self, other):
        return self.hit_hat() != other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

    def __gt__(self, other):
        return self.hit_hat() > other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __ge__(self, other):
        return self.hit_hat() >= other.hit_hat()

    def add_garage(self, garage: Garage):
        if garage.owner is not None:
            print(f'This garage is the property of the collector - {self.name}')
        else:
            self.garages.append(garage)
            garage.owner = self.register_id

    def most_empty(self):
        most_empty = self.garages[0]
        for i in range(1, len(self.garages)):
            if self.garages[i].free_places > most_empty.free_places:
                most_empty = self.garages[i]
        if most_empty.free_places == 0:
            return None
        return most_empty

    def add_car(self, car: Car, garage: Garage = None):
        if garage is not None:
            if garage in self.garages:
                garage.add(car)
            else:
                print(f'Sorry, {self.name} does not have this garage')
        else:
            most_empty(self).add(car)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(map(lambda garage: len(garage.cars), self.garages))

    def hit_hat(self):
        return sum(map(lambda garage: garage.hit_hat(), self.garages))









