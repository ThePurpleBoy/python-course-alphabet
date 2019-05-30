import unittest
import uuid
from objects import Car, Garage, Cesar
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS


class CarTest(unittest.TestCase):

    def test_init(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsInstance(car.price, float)
        self.assertIsInstance(car.mileage, float)
        self.assertIn(car.producer, CARS_PRODUCER)
        self.assertIn(car.car_type, CARS_TYPES)
        self.assertIsNone(car.garage)
        self.assertIsNone(car.owner)
        self.assertIsInstance(car.number, uuid.UUID)

    def test_eq(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Coupe", 10, 1)
        self.assertEqual(car1, car2, msg="test_eq - OK")

    def test_ne(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Coupe", 20, 1)
        self.assertNotEqual(car1, car2)

    def test_lt(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Coupe", 20, 1)
        self.assertLess(car1, car2)

    def test_gt(self):
        car1 = Car("Ford", "Sedan", 20, 1)
        car2 = Car("Ford", "Coupe", 10, 1)
        self.assertGreater(car1, car2)

    def test_le(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Coupe", 20, 1)
        car3 = Car("Ford", "Coupe", 10, 2)
        self.assertLessEqual(car1, car2)
        self.assertLessEqual(car1, car3)

    def test_ge(self):
        car1 = Car("Ford", "Sedan", 20, 1)
        car2 = Car("Ford", "Coupe", 10, 1)
        car3 = Car("Ford", "Coupe", 20, 2)
        self.assertGreaterEqual(car1, car2)
        self.assertGreaterEqual(car1, car3)

    def test_str(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        self.assertIsInstance(str(car1), str)
        self.assertMultiLineEqual(str(car1), f"Ford - Sedan, Price:10.0, Mileage:1.0, Number:{car1.number}")

    def test_repr(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        self.assertIsInstance(repr(car1), str)
        self.assertMultiLineEqual(repr(car1), f"< Ford / Sedan / 10.0 / 1.0 / {car1.number} >")


if __name__ == "__main__":
    unittest.main()