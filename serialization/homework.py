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
import sys
from typing import List
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS
from uuid import uuid4
import json
import pickle
from ruamel.yaml import YAML, yaml_object
from ruamel.yaml.compat import StringIO


class NewYaml(YAML):  # This class would not appear here without Pavlo Zubariev's help !
    def dump(self, data, stream=None, **kw):
        inefficient = False
        if stream is None:
            inefficient = True
            stream = StringIO()
        YAML.dump(self, data, stream, **kw)
        if inefficient:
            return stream.getvalue()


yaml = NewYaml()


@yaml_object(yaml)
class Car:
    yaml = NewYaml()

    def __init__(self, producer, car_type, price: float, mileage: float):
        if producer not in CARS_PRODUCER:
            raise ValueError(f'Producer: <{producer}> is not available. Select a producer from the following list {CARS_PRODUCER}')
        if car_type not in CARS_TYPES:
            raise ValueError(f'Car_type: <{car_type}> is not available. Select a car_type from the following list {CARS_TYPES}')

        self.producer = producer
        self.car_type = car_type
        self.price = float(price)
        self.mileage = float(mileage)
        self.number = uuid4().hex
        self.owner = None

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
        return f"Producer: {self.producer}, Car_type: {self.car_type}, Price: {self.price}, Mileage: {self.mileage}, Number: {self.number}"

    def replace_number(self):
        self.number = uuid4().hex

    @staticmethod
    def json_default(obj):  # encoder
        data = {"producer": obj.producer,
                "car_type": obj.car_type,
                "price": obj.price,
                "mileage": obj.mileage,
                "number": obj.number,
                "owner": obj.owner}
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
        car.owner = data.get('owner')
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

    def pickle_serialize_to_string(self):
        return pickle.dumps(self)

    def pickle_serialize_to_file(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def pickle_deserialize_from_string(obj):
        return pickle.loads(obj)

    @staticmethod
    def pickle_deserialize_from_file(pickle_file):
        with open(pickle_file, 'rb') as file:
            return pickle.load(file)

    def yaml_serialise_to_string(self):
        return yaml.dump(self)

    def yaml_serialize_to_file(self, file_name):
        with open(file_name, 'w') as file:
            yaml.dump(self, file)

    @staticmethod
    def yaml_deserialize_from_string(obj):
        return yaml.load(obj)

    @staticmethod
    def yaml_deserialize_from_file(yaml_file):
        with open(yaml_file, 'r') as file:
            return yaml.load(file)


@yaml_object(yaml)
class Garage:
    yaml = NewYaml()
    cars: List[Car]

    def __init__(self, town, places: int, cars=None):
        if town not in TOWNS:
            raise ValueError(f'Town: <{town}> is not available. Select a town from the following list {TOWNS}')
        if places <= 0:
            raise ValueError(f'Places should be a positive number')
        if cars and len(cars) > places:
            raise ValueError(f'There is not enough space for all cars in the garage. Free places = {places}, Cars = {len(cars)}')
        if cars is None:
            self.cars = []
        else:
            for car in cars:
                if car.garage:
                    raise ValueError(f'Car: {car} not available')
                car.garage = self
            self.cars = cars

        self.town = town
        self.places = places
        self.owner = None
        self.free_places = self.places - len(self.cars)

    def __str__(self):
        return f"{self.town}, {self.places}, {self.cars}, {self.owner}"

    def __repr__(self):
        return f"Town: {self.town}, Places: {self.places}, Cars: {self.cars}, Owner: {self.owner} >"

    def add(self, car: Car):
        if self.free_places == 0:
            raise ValueError("Sorry, no room for a new car")
        elif car.garage:
            raise ValueError(f"This car {car} is part of another garage")
        else:
            self.cars.append(car)
            car.garage = self

    def remove(self, car: Car):
        if car not in self.cars:
            raise ValueError(f"This car: {car} is not in this garage")
        else:
            self.cars.remove(car)
            car.garage = None

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
        cars = json.loads(data['cars'], object_hook=Car.json_hook)
        garage = Garage(town=town,
                        places=places,
                        cars=cars)
        garage.free_places = data.get('free_places')
        garage.owner = data.get('owner')
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

    def pickle_serialize_to_string(self):
        return pickle.dumps(self)

    def pickle_serialize_to_file(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def pickle_deserialize_from_string(obj):
        return pickle.loads(obj)

    @staticmethod
    def pickle_deserialize_from_file(pickle_file):
        with open(pickle_file, 'rb') as file:
            return pickle.load(file)

    def yaml_serialise_to_string(self):
        return yaml.dump(self)

    def yaml_serialize_to_file(self, file_name):
        with open(file_name, 'w') as file:
            yaml.dump(self, file)

    @staticmethod
    def yaml_deserialize_from_string(obj):
        return yaml.load(obj)

    @staticmethod
    def yaml_deserialize_from_file(yaml_file):
        with open(yaml_file, 'r') as file:
            return yaml.load(file)


@yaml_object(yaml)
class Cesar:
    yaml = NewYaml()
    garages = List[Garage]

    def __init__(self, name: str, garages=None):
        self.name = name
        self.register_id = uuid4().hex
        if garages is None:
            self.garages = []
        else:
            for garage in garages:
                if garage.owner is not None:
                    raise ValueError(f'This garage: {garage} is the property of another collector (id = {garage.owner})')
                garage.owner = self.register_id
                for car in garage.cars:
                    car.owner = self.register_id
                    car.garage = garage
            self.garages = garages

    def __str__(self):
        return f'{self.name}: {self.garages}/ {self.register_id}'

    def __repr__(self):
        return f'Name: {self.name}, Garages: {self.garages}, Register_id: {self.register_id}'

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
        if garage.owner:
            raise ValueError(f'This garage: {garage} is the property of the other collector (id = {garage.owner})')
        else:
            self.garages.append(garage)
            garage.owner = self.register_id
            for car in garage.cars:
                car.owner = self.register_id

    def most_empty(self):
        return max(self.garages, key=lambda garage: garage.free_places)

    def add_car(self, car: Car, garage: Garage = None):
        if car.garage:
            raise ValueError('This machine is already in use')
        elif garage is None:
            self.most_empty().add(car)
        elif garage not in self.garages:
            raise ValueError(f'This garage: {garage} is the property of the other collector (id = {garage.owner})')
        elif garage.free_places == 0:
            raise ValueError('There are no free places in the specified garage')
        else:
            garage.add(car)

    def garages_count(self):
        return len(self.garages)

    def cars_count(self):
        return sum(map(lambda garage: len(garage.cars), self.garages))

    def hit_hat(self):
        return sum(map(lambda garage: garage.hit_hat(), self.garages))

    @staticmethod
    def json_default(obj):  # encoder
        garages = json.dumps(obj.garages, default=Garage.json_default)
        data = {'name': obj.name,
                'garages': garages,
                'register_id': obj.register_id}
        return data

    @classmethod
    def json_hook(cls, data):  # decoder
        name = data['name']
        garages = json.loads(data['garages'], object_hook=Garage.json_hook)
        cesar = Cesar(name=name,
                      garages=garages)
        cesar.register_id = data.get('register_id')
        return cesar

    def json_serialize_to_string(self):
        return json.dumps(self, default=Cesar.json_default, indent=4)

    def json_serialize_to_file(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self, file, default=Cesar.json_default, indent=4)

    @staticmethod
    def json_deserialize_from_string(obj):
        return json.loads(obj, object_hook=Cesar.json_hook)

    @staticmethod
    def json_deserialize_from_file(json_file):
        with open(json_file, 'r') as file:
            return json.load(file, object_hook=Cesar.json_hook)

    def pickle_serialize_to_string(self):
        return pickle.dumps(self)

    def pickle_serialize_to_file(self, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def pickle_deserialize_from_string(obj):
        return pickle.loads(obj)

    @staticmethod
    def pickle_deserialize_from_file(pickle_file):
        with open(pickle_file, 'rb') as file:
            return pickle.load(file)

    def yaml_serialise_to_string(self):
        return yaml.dump(self)

    def yaml_serialize_to_file(self, file_name):
        with open(file_name, 'w') as file:
            yaml.dump(self, file)

    @staticmethod
    def yaml_deserialize_from_string(obj):
        return yaml.load(obj)

    @staticmethod
    def yaml_deserialize_from_file(yaml_file):
        with open(yaml_file, 'r') as file:
            return yaml.load(file)





