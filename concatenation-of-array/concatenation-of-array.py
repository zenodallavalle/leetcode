class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i =  0
        while i < (len(nums) - i):
            nums.append(nums[i])
            i+=1
        return nums