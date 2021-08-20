class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        i = 0
        while i <len(nums):
            element = nums[i]
            delta = target-element
            if delta in previous:
                return previous[delta], i
            else:
                previous[element] = i
            i+=1