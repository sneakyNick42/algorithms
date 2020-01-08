"""Abstract base classes for future inheritance"""
from abc import ABCMeta, abstractmethod
from typing import List


class Search(metaclass=ABCMeta):
    """
    Abstract base class for searching algorithms
    """
    # pylint:disable=too-few-public-methods

    def __init__(self, array: List[int]) -> None:
        self.array = array

    @abstractmethod
    def search(self, desired: int) -> bool:
        """Search desired: int in self.array. Return True if found, False otherwise"""


class Sort(metaclass=ABCMeta):
    """
    Abstract base class for sorting algorithms
    """
    # pylint:disable=too-few-public-methods

    def __init__(self, array: List[int]) -> None:
        self.array = array

    @abstractmethod
    def sort(self) -> List[int]:
        """Sort self.array. Return sorted array: List[int]"""
