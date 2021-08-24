class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # First solution time O(nlog(n)) space O(1)
        # nums.sort()
        # i = 0
        # while (i+1) < len(nums):
        #     if nums[i] == nums[i+1]:return True
        #     i+=1
        # return False
        
        # Second solution time O(N) space O(N)
        ht = {}
        for n in nums:
            if n in ht:
                return True
            else:
                ht[n] = None
        return False