class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #replace numbers with the largest number from the right
        newList = []
        for i in range(len(arr)-1):
            pop = 0
            pop += 1
            arr.pop(0)
            for j in range(len(arr)):
                d = max(arr)

            newList.append(d)
        newList.append(-1)
        return newList


        