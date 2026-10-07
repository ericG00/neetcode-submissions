class Solution:
    def isHappy(self, n: int) -> bool:
        valuesSeen = []

        while n != 1:
            count = 0
            changedType = str(n)
            for i in changedType:
                count += int(i)**2

            n = count
            if count in valuesSeen:
                return False
            else:
                valuesSeen.append(count)

        return True
        



            