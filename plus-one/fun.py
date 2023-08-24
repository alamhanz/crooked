from typing import List


class Solution:
    """Solution Class

    Args:
        bin_file (_type_): _description_

    Returns:
        _type_: decoded content.
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        """PlusOne Solution

        Args:
            digits (List): list of integers between 0 and 9

        Returns:
            List : list of integers plus one
        """
        if len(digits) > 0:
            digits[-1] += 1
            if digits[-1] < 10:
                return digits
            else:
                return self.plusOne(digits[:-1]) + [0]
        else:
            return [1]
