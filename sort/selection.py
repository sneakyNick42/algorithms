"""Selection search"""
from typing import List

from base import Sort


class Selection(Sort):
    """
    Selection sort class
    """
    # pylint:disable=too-few-public-methods

    def sort(self) -> List[int]:
        result_array = []

        for _ in range(len(self.array)):
            smallest = self.find_smallest()
            result_array.append(self.array.pop(smallest))
        return result_array

    def find_smallest(self) -> int:
        """Find lowest index in self.array"""
        lowest = self.array[0]
        lowest_index = 0

        for i in range(1, len(self.array)):
            if self.array[i] < lowest:
                lowest = self.array[i]
                lowest_index = i
        return lowest_index
