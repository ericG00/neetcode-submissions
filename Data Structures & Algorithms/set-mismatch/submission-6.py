class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counting = Counter(nums)
        target = [0,0]

        for i in range(1, len(nums)+1):
            if counting[i] == 0:
                target[1] = i
            if counting[i] == 2:
                target[0] = i


        return target



      



            
        


        