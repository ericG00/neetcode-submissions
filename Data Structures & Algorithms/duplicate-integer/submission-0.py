class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #check if the number in array appears more than once

        mengde = set()
        for i in nums:
            mengde.add(i)

        #True if the new list has a duplicate 
        if len(mengde) == len(nums):
            return False
        return True


        