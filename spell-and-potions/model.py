class Solution:
    # def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    def successfulPairs(self, spells, potions, success):
        hocuspocus = lambda a,b: [[r*q for r in p] for p, q in zip(a,b)]


# def bisectLeft(nums, target):
#         """
#         Returns leftmost insertion point that target should be inserted in the sorted array
#         """
#         left, right = 0, len(nums)
        
#         while left < right:
#             mid = left + (right - left) // 2
            
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
            
#         return left


def hocu(nums, succ, multi):
    nums.sort()
    nums2 = [i*multi for i in nums]
    succ2 = (succ + multi - 1)//multi
    succ3 = succ//multi
    return nums2, succ, nums, succ2, succ3