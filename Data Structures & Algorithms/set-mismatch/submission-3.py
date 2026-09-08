class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #find the number that is a duplicate and the missing number
        #the missing number is any R
        #take out the duplicate
        #make a new list with the length of nums 
        #go through the new list and find the number which is not in nums
        
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



      



            
        


        