class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove non alphabets
        removeNonAlph = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                removeNonAlph += i
        # removes space on string 
        removedSpace = removeNonAlph.replace(" ", "")

        # reverse the sentece
        reverse = ""
        for i in s[::-1]:
            if i.isalpha() or i.isdigit():
                reverse += i
        
        # remove space on the reversed sentence
        repReversed = reverse.replace(" ", "")

        a = removedSpace.lower()
        b = repReversed.lower()
        
        # checks if the words are identical 
        print(a,b)
        return a == b


        



        

        