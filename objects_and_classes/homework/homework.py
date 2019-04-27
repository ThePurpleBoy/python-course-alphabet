"""
Вам небхідно написати 3 класи. Мільйонери Гаражі та Автомобілі.
Звязкок наступний один мільйонер може мати багато гаражів.
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
import random
import uuid

CARS_TYPES = ["SUV", "Truck", "Sedan", "Van", "Coupe", "Wagon", "Sports Car", "Diesel", "Crossover", "Luxury Car"]
CARS_PRODUCER = ["BENTLEY", "BMW", "Bugatti", "Buick", "Chery", "Chevrolet", "Dodge", "Ford", "Lamborghini"]

TOWNS = ["Amsterdam", "Kiev", "Prague", "Rome", "Paris", "London", "Berlin"]


class Car:

    def __init__(self, number=uuid.uuid4()):
        self.type = random.choice(CARS_TYPES)
        self.producer = random.choice(CARS_PRODUCER)
        self.price = round(random.uniform(10000, 500000), 2)
        self.mileage = round(random.uniform(0, 100000), 2)
        self.number = number.hex

    def __eq__(self, other: Car):
        return self.price == other.price

    def __ne__(self, other: Car):
        return self.price != other.price

    def __lt__(self, other: Car):
        return self.price < other.price

    def __gt__(self, other: Car):
        return self.price > other.price

    def __le__(self, other: Car):
        return self.price <= other.price

    def __ge__(self, other: Car):
        return self.price >= other.price

    def __str__(self):
        return f"{self.type}, {self.producer}, {self.price}, {self.mileage}, {self.number}"

    def replace_number(self):
        self.number = uuid.uuid4().hex











class Garage:

    def __init__(self, cars=[], owner=None):
        self.town = random.choice(TOWNS)
        self.cars = cars
        self.places = random.randint(3, 20)
        self.owner = owner

    def add(self, car: Car):
        self.cars.append(car)
        self.places -= 1

    def remove(self, car: Car):
        self.cars.remove(car)
        self.places += 1

    def hit_hat(self):
        return sum(map(lambda car: car.price, self.cars))
































class Millionaire:

    def __init__(self, name, garages=[], register_id=uuid.uuid4()):
        self.name = name
        self.register_id = register_id.hex
        self.garages = garages

    def garages_count(self):
        return len(self.garages)

    def add_garage(self, garage: Garage):
        self.garages.append(garage)

    def add_car(self, car: Car):



    def cars_count(self):









