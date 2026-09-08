class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        target = list()
        mengde = list()

        for i in nums:
            if i not in mengde:
                mengde.append(i)
            else:
                target.append(i)

        for i in range(1, len(nums)+1):
            if i not in nums:
                target.append(i)

        return target



      



            
        


        