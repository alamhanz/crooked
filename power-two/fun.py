class Solution:
    """_summary_"""

    def isPowerOfTwo(self, n: int) -> bool:
        """_summary_

        Args:
            n (int): _description_

        Returns:
            bool: _description_
        """
        if n <= 2:
            return n in [1, 2]

        new_n, remainder = divmod(n, 2)

        if remainder == 0:
            return self.isPowerOfTwo(new_n)
        return False


## best solutions is using binary operations
