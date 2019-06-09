import unittest
import uuid
from objects import Car, Garage, Cesar
from objects_and_classes.homework.constants import CARS_TYPES, CARS_PRODUCER, TOWNS


class TestCarInit(unittest.TestCase):

    def test_valid_producer(self):
        car = Car("Ford", "Sedan", 10, 1)
        actual = car.producer
        expected = "Ford"
        self.assertEqual(actual, expected)

    def test_invalid_producer(self):
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            car = Car("Invalid_data", "Sedan", 10, 1)
        self.assertTrue(f'Producer: <Invalid_data> is not available. '
                        f'Select a producer from the following list {CARS_PRODUCER}'
                        in context.exception.args)

    def test_valid_car_type(self):
        car = Car("Ford", "Sedan", 10, 1)
        actual = car.car_type
        expected = "Sedan"
        self.assertEqual(actual, expected)

    def test_invalid_car_type(self):
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            car = Car("Ford", "Invalid_data", 10, 1)
        self.assertTrue(f'Car_type: <Invalid_data> is not available. '
                        f'Select a car_type from the following list {CARS_TYPES}'
                        in context.exception.args)

    def test_valid_price(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsInstance(car.price, float)
        self.assertGreater(car.price, 0, msg="Negative price")

    def test_valid_mileage(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsInstance(car.mileage, float)
        self.assertGreaterEqual(car.mileage, 0, msg="Negative mileage")

    def test_valid_number(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsInstance(car.number, str)
        self.assertIsNotNone(car.number)

    def test_valid_garage(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsNone(car.garage)

    def test_valid_owner(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsNone(car.owner)


class TestCarOutput(unittest.TestCase):

    def test_str(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        actual = str(car1)
        expected = f"Ford - Sedan, Price:10.0, Mileage:1.0, Number:{car1.number}"
        self.assertIsInstance(str(car1), str)
        self.assertMultiLineEqual(actual, expected)

    def test_repr(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        actual = repr(car1)
        expected = f"< Ford / Sedan / 10.0 / 1.0 / {car1.number} >"
        self.assertIsInstance(repr(car1), str)
        self.assertMultiLineEqual(actual, expected)


class TestCarComparison(unittest.TestCase):

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





if __name__ == "__main__":
    unittest.main()
