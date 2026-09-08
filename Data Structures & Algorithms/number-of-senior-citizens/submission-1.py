class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            for j in range(len(details[i])-1):
                if j == 11:
                    age = int(details[i][j] + details[i][j+1])
                    if age > 60:
                        count += 1
        return count

        