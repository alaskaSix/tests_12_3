import unittest
from tests_12_3 import RunnerTest, Tournament


loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(Tournament))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)