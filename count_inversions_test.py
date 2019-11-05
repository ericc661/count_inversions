import unittest

from count_inversions import InversionCounter

class test_count_inversions(unittest.TestCase):

    def setUp(self):
        self.ic = InversionCounter()

    # trivial TestCase
    def test1(self):
        (count, list) = self.ic.count_inversions([1])
        self.assertEqual(1, 0)
        self.assertEqual(count, 0)
        self.assertEqual(list, [1])

    # 1 inversion, input size 3
    def test2(self):
        (count, list) = self.ic.count_inversions([1, 3, 2])
        self.assertEqual(count, 1)
        self.assertEqual(list, [1, 2, 3])

    # input size 5, 7 inversions
    def test3(self):
        (count, list) = self.ic.count_inversions([5, 4, 1, 2, 3])
        self.assertEqual(count, 7)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    # input size 5, completely inverted (10)
    def test4(self):
        (count, list) = self.ic.count_inversions([5, 4, 3, 2, 1])
        self.assertEqual(count, 10)
        self.assertEqual(list, [1, 2, 3, 4, 5])

    # input size 5, no inversions
    def test5(self):
        (count, list) = self.ic.count_inversions([1, 2, 3, 4, 5])
        self.assertEqual(count, 0)
        self.assertEqual(list, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
