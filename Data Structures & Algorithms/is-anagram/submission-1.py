class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the words in s is a anagram in t
        sortS = sorted(s)
        sortT = sorted(t)

        if sortS == sortT:
            return True 
        return False
        