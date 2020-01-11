"""Quick sort"""
from typing import List

from base import Sort


class Quick(Sort):
    """
    Quick sort class
    """

    # pylint:disable=too-few-public-methods

    def sort(self) -> List[int]:
        if len(self.array) < 2:
            return self.array

        middle_index = int((len(self.array) - 1) / 2)
        pivot = self.array[middle_index]
        less = [i for i in self.array if i < pivot]
        more = [i for i in self.array if i > pivot]

        return Quick(less).sort() + [pivot] + Quick(more).sort()
