class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingNum = 0
        for i in range(len(nums)):
            if i not in nums:
                missingNum = i
                break
            else:
                missingNum = len(nums)

        return missingNum

        