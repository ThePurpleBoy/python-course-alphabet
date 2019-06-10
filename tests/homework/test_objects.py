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

    def test_number(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsInstance(car.number, str)
        self.assertIsNotNone(car.number)

    def test_garage(self):
        car = Car("Ford", "Sedan", 10, 1)
        self.assertIsNone(car.garage)

    def test_owner(self):
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
        car1 = Car("Ford", "Sedan", 10, 1)      # 10
        car2 = Car("Ford", "Coupe", 10, 1)      # 10
        self.assertEqual(car1, car2)        # 10 == 10

    def test_ne(self):
        car1 = Car("Ford", "Sedan", 10, 1)      # 10
        car2 = Car("Ford", "Coupe", 20, 1)      # 20
        self.assertNotEqual(car1, car2)     # 10 != 20

    def test_lt(self):
        car1 = Car("Ford", "Sedan", 10, 1)      # 10
        car2 = Car("Ford", "Coupe", 20, 1)      # 10
        self.assertLess(car1, car2)         # 10 < 20

    def test_gt(self):
        car1 = Car("Ford", "Sedan", 10, 1)      # 10
        car2 = Car("Ford", "Coupe", 20, 1)      # 20
        self.assertGreater(car2, car1)      # 20 > 10

    def test_le(self):
        car1 = Car("Ford", "Sedan", 10, 1)      # 10
        car2 = Car("Ford", "Coupe", 20, 1)      # 20
        car3 = Car("Ford", "Coupe", 10, 2)      # 10
        self.assertLessEqual(car1, car2)    # 10 < 20
        self.assertLessEqual(car1, car3)    # 10 == 10

    def test_ge(self):
        car1 = Car("Ford", "Sedan", 20, 1)      # 20
        car2 = Car("Ford", "Coupe", 10, 1)      # 10
        car3 = Car("Ford", "Coupe", 20, 2)      # 20
        self.assertGreaterEqual(car1, car2)     # 20 > 10
        self.assertGreaterEqual(car1, car3)     # 20 == 20


class TestGarageInit(unittest.TestCase):

    def test_valid_towns(self):
        garage = Garage("London", 5)
        actual = garage.town
        expected = "London"
        self.assertEqual(actual, expected)

    def test_invalid_towns(self):
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            garage = Garage("Invalid_data", 5)
        self.assertTrue(f'Town: <Invalid_data> is not available. '
                        f'Select a town from the following list {TOWNS}'
                        in context.exception.args)

    def test_valid_places(self):
        garage = Garage("London", 5)
        actual = garage.places
        expected = 5
        self.assertEqual(actual, expected)
        self.assertIsInstance(garage.places, int)
        self.assertGreater(garage.places, 0, msg="The value should be greater than zero")

    def test_invalid_places(self):
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            garage = Garage("London", -5)
        self.assertTrue(f'Places should be a positive number' in context.exception.args)

    def test_empty_garage(self):
        garage_empty = Garage("London", 5)
        actual = garage_empty.cars
        expected = []
        self.assertEqual(actual, expected)

    def test_valid_cars(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        garage = Garage("London", 5, [car1, car2])
        actual = garage.cars
        expected = [car1, car2]
        self.assertEqual(actual, expected)

    def test_to_many_cars(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            garage = Garage("London", 1, [car1, car2])
        self.assertTrue(f'There is not enough space for all cars in the garage. '
                        f'Free places = 1, Cars = 2'
                        in context.exception.args)

    def test_inaccessible_car(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage1 = Garage("London", 5, [car])
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            garage2 = Garage("London", 1, [car])
        self.assertTrue(f'Car: {car} not available' in context.exception.args)

    def test_owner(self):
        garage = Garage("London", 5)
        self.assertIsNone(garage.owner)

    def test_free_places(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 5, [car])
        actual = garage.free_places
        expected = 4
        self.assertEqual(actual, expected)


class TestGarageOutput(unittest.TestCase):

    def test_str(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        garage = Garage("London", 5, [car1, car2])
        actual = str(garage)
        expected = f"London, 5, [< Ford / Sedan / 10.0 / 1.0 / {car1.number} >, " \
                            f"< Ford / Sedan / 20.0 / 2.0 / {car2.number} >], None"
        self.assertEqual(actual, expected)

    def test_repr(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        garage = Garage("London", 5, [car1, car2])
        actual = repr(garage)
        expected = f"< London, 5, [< Ford / Sedan / 10.0 / 1.0 / {car1.number} >, " \
                                f"< Ford / Sedan / 20.0 / 2.0 / {car2.number} >], None >"
        self.assertEqual(actual, expected)


class TestGarageMethods(unittest.TestCase):

    def test_add_valid(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 5)
        garage.add(car)
        actual = [car]
        expected = garage.cars
        self.assertEqual(actual, expected)
        self.assertEqual(car.garage, garage)

    def test_add_no_free_places(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 1)
        garage.free_places = 0
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            garage.add(car)
        self.assertTrue("Sorry, no room for a new car" in context.exception.args)

    def test_add_inaccessible_car(self):
        car = Car("Ford", "Sedan", 10, 1)
        car.garage = True
        garage = Garage("London", 10)
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            garage.add(car)
        self.assertTrue(f"This car {car} is part of another garage" in context.exception.args)

    def test_remove_valid(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 5, [car])
        garage.remove(car)
        actual = []
        expected = garage.cars
        self.assertEqual(actual, expected)
        self.assertIsNone(car.owner)

    def test_remove_inaccessible_car(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 10)
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            garage.remove(car)
        self.assertTrue(f"This car: {car} is not in this garage" in context.exception.args)

    def test_hit_hat(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        garage = Garage("London", 5, [car1, car2])
        actual = garage.hit_hat()
        expected = 30
        self.assertEqual(actual, expected)


class TestCesarInit(unittest.TestCase):

    def test_name(self):
        cesar = Cesar("Yulii")
        actual = "Yulii"
        expected = cesar.name
        self.assertEqual(actual, expected)

    def test_register_id(self):
        cesar = Cesar("Yulii")
        self.assertIsInstance(cesar.register_id, str)
        self.assertIsNotNone(cesar.register_id)

    def test_empty_cars(self):
        cesar = Cesar("Yulii")
        actual = []
        expected = cesar.garages
        self.assertEqual(actual, expected)

    def test_valid_garages(self):
        garage1 = Garage("London", 5)
        garage2 = Garage("London", 10)
        cesar = Cesar("Yulii", [garage1, garage2])
        actual = cesar.garages
        expected = [garage1, garage2]
        self.assertEqual(actual, expected)

    def test_inaccessible_garage(self):
        garage = Garage("London", 5)
        garage.owner = True
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            cesar = Cesar("Brutus", [garage])
        self.assertTrue(f'This garage: {garage} is the property of another collector (id = {garage.owner})'
                        in context.exception.args)


class TestCesarOutput(unittest.TestCase):

    def test_str(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        garage1 = Garage("London", 5, [car1])
        garage2 = Garage("London", 10, [car2])
        cesar = Cesar("Yulii", [garage1, garage2])

        actual = str(cesar)
        expected = f"Yulii: [< London, 5, [< Ford / Sedan / 10.0 / 1.0 / {car1.number} >], {garage1.owner} >, " \
                            f"< London, 10, [< Ford / Sedan / 20.0 / 2.0 / {car2.number} >], {garage2.owner} >]/ " \
                            f"{cesar.register_id}"
        self.assertEqual(actual, expected)

    def test_repr(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        garage1 = Garage("London", 5, [car1])
        garage2 = Garage("London", 10, [car2])
        cesar = Cesar("Yulii", [garage1, garage2])

        actual = repr(cesar)
        expected = f"Yulii/ [< London, 5, [< Ford / Sedan / 10.0 / 1.0 / {car1.number} >], {garage1.owner} >, " \
                            f"< London, 10, [< Ford / Sedan / 20.0 / 2.0 / {car2.number} >], {garage2.owner} >]/ " \
                            f"{cesar.register_id}"
        self.assertEqual(actual, expected)


class TestCesarComparison(unittest.TestCase):

    def test_eq(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        car4 = Car("Ford", "Sedan", 40, 4)
        garage1 = Garage("London", 5, [car1, car4])
        garage2 = Garage("London", 10, [car2, car3])
        cesar1 = Cesar("Yulii", [garage1])      # 50
        cesar2 = Cesar("Brutus", [garage2])     # 50
        self.assertEqual(cesar1, cesar2)        # 50 == 50

    def test_ne(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        car4 = Car("Ford", "Sedan", 40, 4)
        garage1 = Garage("London", 5, [car1, car2])
        garage2 = Garage("London", 10, [car3, car4])
        cesar1 = Cesar("Yulii", [garage1])      # 30
        cesar2 = Cesar("Brutus", [garage2])     # 70
        self.assertNotEqual(cesar1, cesar2)     # 30 != 70

    def test_lt(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        car4 = Car("Ford", "Sedan", 40, 4)
        garage1 = Garage("London", 5, [car1, car2])
        garage2 = Garage("London", 10, [car3, car4])
        cesar1 = Cesar("Yulii", [garage1])      # 30
        cesar2 = Cesar("Brutus", [garage2])     # 70
        self.assertLess(cesar1, cesar2)     # 30 < 70

    def test_gt(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        car4 = Car("Ford", "Sedan", 40, 4)
        garage1 = Garage("London", 5, [car1, car2])
        garage2 = Garage("London", 10, [car3, car4])
        cesar1 = Cesar("Yulii", [garage1])      # 30
        cesar2 = Cesar("Brutus", [garage2])     # 70
        self.assertGreater(cesar2, cesar1)  # 70 > 30

    def test_le(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        car4 = Car("Ford", "Sedan", 40, 4)
        garage1 = Garage("London", 5, [car1, car2])
        garage2 = Garage("London", 10, [car3])
        garage3 = Garage("London", 10, [car4])
        cesar1 = Cesar("Yulii", [garage1])      # 30
        cesar2 = Cesar("Brutus", [garage2])     # 30
        cesar3 = Cesar("Mark", [garage3])       # 40

        self.assertLessEqual(cesar1, cesar2)    # 30 == 30
        self.assertLessEqual(cesar1, cesar3)    # 30 < 40

    def test_ge(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        car4 = Car("Ford", "Sedan", 40, 4)
        garage1 = Garage("London", 5, [car1, car2])
        garage2 = Garage("London", 10, [car3])
        garage3 = Garage("London", 10, [car4])
        cesar1 = Cesar("Yulii", [garage1])      # 30
        cesar2 = Cesar("Brutus", [garage2])     # 30
        cesar3 = Cesar("Mark", [garage3])       # 40

        self.assertGreaterEqual(cesar1, cesar2)     # 30 == 30
        self.assertGreaterEqual(cesar3, cesar1)     # 40 > 30


class TestCesarMethods(unittest.TestCase):

    def test_add_garage_valid(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 5, [car])
        cesar = Cesar("Yulii")
        cesar.add_garage(garage)
        actual = [garage]
        expected = cesar.garages
        self.assertEqual(actual, expected)
        self.assertEqual(garage.owner, cesar.register_id)
        self.assertEqual(car.owner, cesar.register_id)

    def test_add_garage_inaccessible_garage(self):
        garage = Garage("London", 5)
        garage.owner = True
        cesar = Cesar("Brutus")
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            cesar.add_garage(garage)
        self.assertTrue(f'This garage: {garage} is the property of the other collector (id = {garage.owner})'
                        in context.exception.args)

    def test_most_empty(self):
        garage1 = Garage("London", 5)
        garage2 = Garage("London", 10)
        cesar = Cesar("Yulii", [garage1, garage2])
        actual = cesar.most_empty()
        expected = garage2
        self.assertEqual(actual, expected)

    def test_add_car_valid(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 5)
        cesar = Cesar("Yulii", [garage])
        cesar.add_car(car, garage)
        actual = cesar.garages[0].cars
        expected = [car]
        self.assertEqual(actual, expected)

    def test_add_car_inaccessible_car(self):
        car = Car("Ford", "Sedan", 10, 1)
        car.garage = True
        garage = Garage("London", 10)
        cesar = Cesar("Yulii", [garage])
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            cesar.add_car(car, garage)
        self.assertTrue('This machine is already in use' in context.exception.args)

    def test_add_car_not_specified(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage1 = Garage("London", 5)
        garage2 = Garage("London", 10)
        cesar = Cesar("Yulii", [garage1, garage2])
        cesar.add_car(car)
        actual = garage2.cars
        expected = [car]
        self.assertEqual(actual, expected)

    def test_add_car_inaccessible_garage(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 10)
        cesar = Cesar("Yulii")
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            cesar.add_car(car, garage)
        self.assertTrue(f'This garage: {garage} is the property of the other collector (id = {garage.owner})'
                        in context.exception.args)

    def test_add_car_not_free_places(self):
        car = Car("Ford", "Sedan", 10, 1)
        garage = Garage("London", 1)
        garage.free_places = 0
        cesar = Cesar("Yulii", [garage])
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            cesar.add_car(car, garage)
        self.assertTrue('There are no free places in the specified garage' in context.exception.args)

    def test_garages_count(self):
        garage1 = Garage("London", 5)
        garage2 = Garage("London", 10)
        cesar = Cesar("Yulii", [garage1, garage2])
        actual = cesar.garages_count()
        expected = 2
        self.assertEqual(actual, expected)

    def test_cars_count(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        garage1 = Garage("London", 5, [car1, car2])
        garage2 = Garage("London", 10, [car3])
        cesar = Cesar("Yulii", [garage1, garage2])

        actual = cesar.cars_count()
        expected = 3
        self.assertEqual(actual, expected)

    def test_hit_hat(self):
        car1 = Car("Ford", "Sedan", 10, 1)
        car2 = Car("Ford", "Sedan", 20, 2)
        car3 = Car("Ford", "Sedan", 30, 3)
        garage1 = Garage("London", 5, [car1, car2])
        garage2 = Garage("London", 10, [car3])
        cesar = Cesar("Yulii", [garage1, garage2])

        actual = cesar.hit_hat()
        expected = 60
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
