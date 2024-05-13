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

# Example usage:
if __name__ == "__main__":
    list1 = InheritanceSortedIntList()
    list1.add(1)
    list1.add(3)
    list1.add(2)
    list1.add(4)
    list1.add(2)
    print(list1.get_total_added())  # Output: 5
    print(list1)  # Output: [1, 2, 2, 3, 4]

    list2 = InheritanceSortedIntList()
    list2.add(3)
    list2.add(0)
    print(list2.get_total_added())  # Output: 2

    list2.add_all(list1)
    print(list2.get_total_added())  # Output: 7
    print(list2)  # Output: [0, 1, 2, 2, 2, 3, 3, 4]