from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # First solution that I thought space O(N) time O(N)
        # return Counter(nums).most_common(1)[0][0]
        
        # Second solution space O(N) time O(N)
        # ht = {}
        # threshold = len(nums)/2
        # for n in nums:
        #     updated = ht.get(n, 0) +1
        #     if updated > threshold:
        #         return n
        #     else:
        #         ht[n] = updated
    
        # Third solution space O(1) time O(nlog(n))
        nums = sorted(nums)
        threshold = len(nums)/2
        start = 0
        i = 0
        while i<len(nums):
            if nums[start] != nums[i]:
                start = i
            else:
                if (i - start + 1) > threshold:
                    return nums[i]
            i+=1