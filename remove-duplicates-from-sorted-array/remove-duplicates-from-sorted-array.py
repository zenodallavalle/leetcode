class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while (i+j) < len(nums):
            if nums[i] != nums[i+j]:
                if j > 1:
                    nums[i+1] = nums[i+j]
                i+=1
            else:
                 j+=1
        return i + 1