from typing import List


class Solution:
    """_summary_"""

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """_summary_

        Args:
            nums (List[int]): _description_
            k (int): _description_

        Returns:
            float: _description_
        """
        nnk = len(nums)
        if k == 1:
            return max(nums)
        elif k == nnk:
            return sum(nums) / k

        total = sum(nums[:k])
        max_avg = total
        for i in range(nnk - k):
            total = total - nums[i] + nums[k + i]
            if total >= max_avg:
                max_avg = total

        return max_avg / k
