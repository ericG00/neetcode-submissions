class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums)//2
        venstreMid = nums[:mid] 
        høyreMid= nums[mid:]
  
        sorterVenstre = self.sortArray(venstreMid)
        sorterHøyre = self.sortArray(høyreMid)
    

        return self.flettArray(sorterVenstre, sorterHøyre)

    def flettArray(self, venstre, høyre):
        res = []
        i = 0
        j = 0

        while i < len(venstre) and j < len(høyre):
            if venstre[i] <= høyre[j]:
                res.append(venstre[i])
                i += 1
            else:
                res.append(høyre[j])
                j += 1
        
        res.extend(venstre[i:])
        res.extend(høyre[j:])

        return res
    
nums=[10,9,1,1,1,2,3,1]
s = Solution()
    

        