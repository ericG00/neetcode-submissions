class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        halfArrayLen = len(nums)//2
        target = 0 
        for k, v in c.items():
            if v > halfArrayLen:
                target = k
        
        return target


            

        