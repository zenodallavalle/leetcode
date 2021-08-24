class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    # First solution I found
    #
    #     nums = sorted(nums)
    #     i, j = 0,1
    #     while j < len(nums):
    #         if nums[i] != nums[j]:return nums[i]
    #         i += 2
    #         j += 2
    #     return nums[-1]
        res = 0
        for n in nums:
            res = res ^ n
        return res