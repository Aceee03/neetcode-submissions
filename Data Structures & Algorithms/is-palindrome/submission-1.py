class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = []
        for c in s:
            if c.isalnum():
                check.append(c)
        
        alphaString = ''.join(check).lower().strip()

        i = 0
        j = len(alphaString)

        while i < j:
            if alphaString[i] != alphaString[j-1]:
                return False
            else:
                i += 1
                j -= 1
                
        return True



        