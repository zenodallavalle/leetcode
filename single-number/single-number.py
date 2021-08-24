class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i, j = 0,1
        while j < len(nums):
            if nums[i] != nums[j]:return nums[i]
            i += 2
            j += 2
        return nums[-1]