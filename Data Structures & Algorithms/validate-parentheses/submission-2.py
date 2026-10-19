class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(',
                ']': '[',
                '}': '{'
        }

        stack = []

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != mapping[char]:
                        return False
        
        return len(stack) == 0
        