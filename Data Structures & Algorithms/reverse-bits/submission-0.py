class Solution:
    def reverseBits(self, n: int) -> int:
        endreStr = format(n, "032b")
        revStr = endreStr[::-1]

        return int(revStr,2)
        

       

        