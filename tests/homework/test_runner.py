import unittest
import test_objects
import test_serialization

CarSuite = unittest.TestSuite()
GarageSuite = unittest.TestSuite()
CesarSuite = unittest.TestSuite()
SerializationSuite = unittest.TestSuite()

CarSuite.addTest(unittest.makeSuite(test_objects.TestCarInit))
CarSuite.addTest(unittest.makeSuite(test_objects.TestCarOutput))
CarSuite.addTest(unittest.makeSuite(test_objects.TestCarComparison))

GarageSuite.addTest(unittest.makeSuite(test_objects.TestGarageInit))
GarageSuite.addTest(unittest.makeSuite(test_objects.TestGarageOutput))
GarageSuite.addTest(unittest.makeSuite(test_objects.TestGarageMethods))

CesarSuite.addTest(unittest.makeSuite(test_objects.TestCesarInit))
CesarSuite.addTest(unittest.makeSuite(test_objects.TestCesarOutput))
CesarSuite.addTest(unittest.makeSuite(test_objects.TestCesarComparison))
CesarSuite.addTest(unittest.makeSuite(test_objects.TestCesarMethods))



runner = unittest.TextTestRunner(verbosity=2)


runner.run(CarSuite)
runner.run(GarageSuite)
runner.run(CesarSuite)

