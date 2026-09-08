class Solution:
    def search(self, nums: List[int], target: int) -> int:
        number = 0
        for i in range(len(nums)):
            if target == nums[i]:
                number = i
                return number
            
        return -1
        
