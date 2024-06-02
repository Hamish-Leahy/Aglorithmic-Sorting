import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort

class TestSortingAlgorithms(unittest.TestCase):
    
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([2, 1]), [1, 2])
        
    def test_merge_sort(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([2, 1]), [1, 2])

if __name__ == '__main__':
    unittest.main()
