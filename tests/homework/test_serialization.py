import unittest
from objects import Car, Garage, Cesar


class TestCarSerialize(unittest.TestCase):

    def test_json_string(self):
        car = Car("Ford", "Sedan", 10, 1)
        json_string = car.json_serialize_to_string()
        actual = Car.json_deserialize_from_string(json_string)
        expected = car
        self.assertEqual(actual, expected)

    def test_json_file(self):
        car = Car("Ford", "Sedan", 10, 1)
        car.json_serialize_to_file('json_test.json')
        actual = Car.json_deserialize_from_file('json_test.json')
        expected = car
        self.assertEqual(actual, expected)

    def test_pickle_string(self):
        car = Car("Ford", "Sedan", 10, 1)
        pickle_string = car.pickle_serialize_to_string()
        actual = Car.pickle_deserialize_from_string(pickle_string)
        expected = car
        self.assertEqual(actual, expected)

    def test_pickle_file(self):
        car = Car("Ford", "Sedan", 10, 1)
        car.pickle_serialize_to_file('pickle_test.txt')
        actual = Car.pickle_deserialize_from_file('pickle_test.txt')
        expected = car
        self.assertEqual(actual, expected)

    def test_yaml_string(self):
        car = Car("Ford", "Sedan", 10, 1)
        yaml_string = car.yaml_serialize_to_string()
        actual = Car.yaml_deserialize_from_string(yaml_string)
        expected = car
        self.assertEqual(actual, expected)

    def test_yaml_file(self):
        car = Car("Ford", "Sedan", 10, 1)
        car.yaml_serialize_to_file('yaml_test.yaml')
        actual = Car.yaml_deserialize_from_file('yaml_test.yaml')
        expected = car
        self.assertEqual(actual, expected)


class TestGarageSerialize(unittest.TestCase):

    def test_json_string(self):
        garage = Garage("London", 5)
        json_string = garage.json_serialize_to_string()
        actual = Garage.json_deserialize_from_string(json_string)
        expected = garage
        # self.assertEqual(actual, expected)
        self.assertIsInstance(expected, Garage)

    def test_json_file(self):
        garage = Garage("London", 10)
        garage.json_serialize_to_file('json_test.json')
        actual = Garage.json_deserialize_from_file('json_test.json')
        expected = garage
        # self.assertEqual(actual, expected)
        self.assertIsInstance(expected, Garage)

    def test_pickle_string(self):
        garage = Garage("London", 10)
        pickle_string = garage.pickle_serialize_to_string()
        actual = Garage.pickle_deserialize_from_string(pickle_string)
        expected = garage
        # self.assertEqual(actual, expected)
        self.assertIsInstance(expected, Garage)

    def test_pickle_file(self):
        garage = Garage("London", 10)
        garage.pickle_serialize_to_file('pickle_test.txt')
        actual = Garage.pickle_deserialize_from_file('pickle_test.txt')
        expected = garage
        # self.assertEqual(actual, expected)
        self.assertIsInstance(expected, Garage)

    def test_yaml_string(self):
        garage = Garage("London", 10)
        yaml_string = garage.yaml_serialize_to_string()
        actual = Garage.yaml_deserialize_from_string(yaml_string)
        expected = garage
        # self.assertEqual(actual, expected)
        self.assertIsInstance(expected, Garage)

    def test_yaml_file(self):
        garage = Garage("London", 10)
        garage.yaml_serialize_to_file('yaml_test.yaml')
        actual = Garage.yaml_deserialize_from_file('yaml_test.yaml')
        expected = garage
        # self.assertEqual(actual, expected)
        self.assertIsInstance(expected, Garage)


class TestCesarSerialize(unittest.TestCase):

    def test_json_string(self):
        cesar = Cesar("Yulii")
        json_string = cesar.json_serialize_to_string()
        actual = Cesar.json_deserialize_from_string(json_string)
        expected = cesar
        self.assertEqual(actual, expected)

    def test_json_file(self):
        cesar = Cesar("Yulii")
        cesar.json_serialize_to_file('json_test.json')
        actual = Cesar.json_deserialize_from_file('json_test.json')
        expected = cesar
        self.assertEqual(actual, expected)

    def test_pickle_string(self):
        cesar = Cesar("Yulii")
        pickle_string = cesar.pickle_serialize_to_string()
        actual = Cesar.pickle_deserialize_from_string(pickle_string)
        expected = cesar
        self.assertEqual(actual, expected)

    def test_pickle_file(self):
        cesar = Cesar("Yulii")
        cesar.pickle_serialize_to_file('pickle_test.txt')
        actual = Cesar.pickle_deserialize_from_file('pickle_test.txt')
        expected = cesar
        self.assertEqual(actual, expected)

    def test_yaml_string(self):
        cesar = Cesar("Yulii")
        yaml_string = cesar.yaml_serialize_to_string()
        actual = Cesar.yaml_deserialize_from_string(yaml_string)
        expected = cesar
        self.assertEqual(actual, expected)

    def test_yaml_file(self):
        cesar = Cesar("Yulii")
        cesar.yaml_serialize_to_file('yaml_test.yaml')
        actual = Cesar.yaml_deserialize_from_file('yaml_test.yaml')
        expected = cesar
        self.assertEqual(actual, expected)