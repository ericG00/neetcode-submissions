class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = 0
        consecutives = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counts += 1
            if nums[i] == 0:
                counts = 0
                continue
            else:
                i < len(nums)
                if counts > consecutives:
                    consecutives = counts
                    
        return consecutives
                