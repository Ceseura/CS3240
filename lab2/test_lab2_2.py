import unittest
from hw2_set import OurSet

class TestSet(unittest.TestCase):

    def setUp(self):
        self.s1 = OurSet()
        self.s1.add_list([1, 3, 5, 7, 9])

        self.s2 = OurSet()
        self.s2.add_list([1, 2, 3, 4, 5])

    def test_union(self):
    	""" 8: union """
    	out1 = self.s1.union(self.s2)

    	self.assertEqual(len(out1), 7, "Union didn't have the correct number of items")

    def test_intersect(self):
    	""" 9: intersection """
    	out2 = self.s1.intersection(self.s2)

    	self.assertEqual(len(out2), 3, "Intersect didn't have the correct number of items")

if __name__ == '__main__':
    unittest.main()