"""Binary search"""
from base import Search


class Binary(Search):
    """
    Binary search class
    """
    # pylint:disable=too-few-public-methods

    def search(self, desired: int) -> int or str:
        first_element = 0
        last_element = len(self.array) - 1

        while first_element <= last_element:
            middle_element = int((first_element + last_element) / 2)
            guess = self.array[middle_element]

            if guess == desired:
                return middle_element
            if guess > desired:
                last_element = middle_element - 1
            else:
                first_element = middle_element + 1

        return 'Not found'
