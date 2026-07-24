class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # try to place nums[i] at its correct spot (value-1)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                 # swap into place
                nums[i], nums[target] = nums[target], nums[i]
        
        for i in range(n):
            # first spot thats wrong
            if nums[i] != i + 1: 
                return i + 1
        # everything was there
        return n + 1