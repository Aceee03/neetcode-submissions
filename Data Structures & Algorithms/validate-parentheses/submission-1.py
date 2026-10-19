class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(',
                ']': '[',
                '}': '{'
        }

        check = []

        for char in s:
            if char in mapping.values():
                check.append(char)
            elif char in mapping.keys():
                if not check or check.pop() != mapping[char]:
                    return False
        
        return len(check) == 0
        