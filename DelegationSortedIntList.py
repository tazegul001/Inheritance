import unittest

class SortedIntList:
    def __init__(self):
        self._data = []

    def add(self, value):
        self._data.append(value)
        self._data.sort()

    def __str__(self):
        return str(self._data)

class InheritanceSortedIntList(SortedIntList):
    def __init__(self):
        super().__init__()
        self.total_added = 0

    def add(self, value):
        super().add(value)
        self.total_added += 1

    def add_all(self, other_list):
        temp = []
        for item in other_list._data:
            temp.append(item)
            self.total_added += 1
        temp.sort()
        for num in temp:
            super().add(num)

    def get_total_added(self):
        return self.total_added

class InheritanceSortedIntListTest(unittest.TestCase):
    def setUp(self):
        self.list1 = InheritanceSortedIntList()
        self.list2 = InheritanceSortedIntList()

    def test_add(self):
        self.list1.add(1)
        self.list1.add(3)
        self.list1.add(2)
        self.list1.add(4)
        self.list1.add(2)
        self.assertEqual(self.list1.get_total_added(), 5)
        self.print_list(self.list1)

    def test_add_all(self):
        self.list1.add(1)
        self.list1.add(3)
        self.list1.add(2)
        self.list1.add(4)
        self.list1.add(2)
        self.assertTrue(self.list1.get_total_added() == 5)

        self.list2.add(3)
        self.list2.add(0)
        self.assertTrue(self.list2.get_total_added() == 2)

        self.list2.add_all(self.list1)
        self.assertTrue(self.list2.get_total_added() == 7)

    def print_list(self, lst):
        for item in lst._data:
            print(item, end=", ")
        print()

if __name__ == "__main__":
    unittest.main()
