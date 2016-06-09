import unittest

class Test_test1(unittest.TestCase):
    def test_B(self):
        self.assertGreater(5,3,"Test Failed")

if __name__ == '__main__':
    unittest.main()