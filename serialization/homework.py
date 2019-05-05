"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

from typing import List
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from uuid import uuid4
import json
import pickle


class Car:

    def __init__(self, producer, car_type, price: float, mileage: float):
        if producer not in CARS_PRODUCER or car_type not in CARS_TYPES:
            print("Please, enter valid values <producer> and <type>")
        else:
            self.producer = producer
            self.car_type = car_type
            self.price = float(price)
            self.mileage = float(mileage)
            self.number = uuid4().hex
            self.usability = True

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
        return f"{self.producer} - {self.car_type}, Price:{self.price}, Mileage:{self.mileage}, Number:{self.number}"

    def __repr__(self):
        return f"< {self.producer} / {self.car_type} / {self.price} / {self.mileage} / {self.number} >"

    def replace_number(self):
        self.number = uuid4().hex

    @staticmethod
    def json_default(obj):  # encoder
        data = {"producer": obj.producer,
                "car_type": obj.car_type,
                "price": obj.price,
                "mileage": obj.mileage,
                "number": obj.number,
                "usability": obj.usability}
        return data


    @classmethod
    def json_hook(cls, data):  # decoder
        producer = data['producer']
        car_type = data['car_type']
        price = data['price']
        mileage = data['mileage']
        car = Car(producer=producer,
                  car_type=car_type,
                  price=price,
                  mileage=mileage)
        car.number = data.get('number')
        car.usability = data.get('usability')
        return car

    def json_serialize_to_string(self):
        return json.dumps(self, default=Car.json_default, indent=4)

    def json_serialize_to_file(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self, file, default=Car.json_default, indent=4)

    @staticmethod
    def json_deserialize_from_string(obj):
        return json.loads(obj, object_hook=Car.json_hook)

    @staticmethod
    def json_deserialize_from_file(json_file):
        with open(json_file, 'r') as file:
            return json.load(file, object_hook=Car.json_hook)


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
            self.free_places = self.places - len(self.cars)
            if cars is not None:
                self.cars = []
                for car in cars:
                    if car not in self.cars:
                        self.cars.append(car)
                        car.usability = False

    def __str__(self):
        return f"{self.town}, {self.places}, {self.cars}, {self.owner}"

    def __repr__(self):
        return f"< {self.town}, {self.places}, {self.cars} >"

    def add(self, car: Car):
        if self.free_places == 0:
            print("Sorry, no room for a new car")
        elif not car.usability:
            print("This car is already in use")
        else:
            self.cars.append(car)
            car.usability = False

    def remove(self, car: Car):
        self.cars.remove(car)
        car.usability = True

    def hit_hat(self):
        return sum(map(lambda car: car.price, self.cars))

    @staticmethod
    def json_default(obj):  # encoder
        cars = json.dumps(obj.cars, default=Car.json_default)
        data = {'town': obj.town,
                'places': obj.places,
                'cars': cars,
                'owner': obj.owner,
                'free_places': obj.free_places}
        return data

    @classmethod
    def json_hook(cls, data):  # decoder
        town = data['town']
        places = data['places']
        owner = data['owner']
        cars = json.loads(data['cars'], object_hook=Car.json_hook)
        garage = Garage(town=town,
                        places=places,
                        cars=cars,
                        owner=owner)
        garage.free_places = data.get('free_places')
        return garage

    def json_serialize_to_string(self):
        return json.dumps(self, default=Garage.json_default, indent=4)

    def json_serialize_to_file(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self, file, default=Garage.json_default, indent=4)

    @staticmethod
    def json_deserialize_from_string(obj):
        return json.loads(obj, object_hook=Garage.json_hook)

    @staticmethod
    def json_deserialize_from_file(json_file):
        with open(json_file, 'r') as file:
            return json.load(file, object_hook=Garage.json_hook)


car1 = Car('Ford', 'Sedan', 222, 11)
car2 = Car('Chery', 'Sedan', 333, 11)
gar1 = Garage('London', 5, [car1, car2])

print(gar1)
# sergar = gar1.json_serialize_to_string()
# print(sergar)
gar1.json_serialize_to_file('test.json')
desgar = Garage.json_deserialize_from_file('test.json')
print(desgar)



class Cesar:

    garages = List[Garage]

    def __init__(self, name: str, garages=None):
        self.name = name
        self.register_id = uuid4().hex
        self.garages = garages if garages is not None else []
        if garages is not None:
            self.garages = []
            for garage in garages:
                if garage not in self.garages:
                    self.garages.append(garage)
                    garage.owner = self.register_id

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
        if not garage.owner:
            print(f'This garage is the property of the other collector')
        else:
            self.garages.append(garage)
            garage.owner = self.register_id

    def most_empty(self):
        empty_gar = self.garages[0]
        for i in range(1, len(self.garages)):
            if self.garages[i].free_places > empty_gar.free_places:
                empty_gar = self.garages[i]
        if empty_gar.free_places == 0:
            return None
        return empty_gar

    def add_car(self, car: Car, garage: Garage = None):
        if garage is not None:
            if garage in self.garages:
                garage.add(car)
            else:
                print(f'Sorry, {self.name} does not have this garage')
        else:
            if most_empty() == None:
                print("There are no free places in any garage")
            else:
                most_empty().add(car)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(map(lambda garage: len(garage.cars), self.garages))

    def hit_hat(self):
        return sum(map(lambda garage: garage.hit_hat(), self.garages))



# car1 = Car('Ford', 'Sedan', 111, 11)
# print(car1)
# car1.json_serialize_to_file('test.json')
# des_car1 = Car.json_deserialize_from_file('test.json')
# print(des_car1)
