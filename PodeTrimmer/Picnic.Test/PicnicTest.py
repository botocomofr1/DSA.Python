import unittest
import SelectionSortIntegers

class Test_Picnic(unittest.TestCase):
    def test_selectionSortIntegers(self):
        SelectionSortIntegers.selection_sort( SelectionSortIntegers.random_list())
        self.assertGreater(5,3,"Test Failed")


if __name__ == '__main__':
    unittest.main()