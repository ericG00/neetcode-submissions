class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #duplicate the existing list in another new list  
        concatenatedList = []
        for i in nums:
            concatenatedList.append(i)
        return concatenatedList + nums