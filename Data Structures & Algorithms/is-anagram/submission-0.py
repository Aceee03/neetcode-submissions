class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}

        if len(s) != len(t):
            return False

        for i,j in zip(s,t):
            s_chars[i] = s_chars.get(i, 0) + 1
            t_chars[j] = t_chars.get(j, 0) + 1
        
        return s_chars == t_chars

            