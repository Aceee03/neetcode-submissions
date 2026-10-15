class Solution:

    def encode(self, strs: List[str]) -> str:
        string = [str(len(s)) + "#" + s for s in strs]
        return ''.join(string)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            for j in range(i, len(s)):
                if s[j] == '#':
                    break

            length = int(s[i:j])
            start = j + 1
            end = start + length

            res.append(s[start:end])
            i = end

        return res
