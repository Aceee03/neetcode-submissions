class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}

        for s in strs:
            sorted_s = sorted(s)
            key = tuple(sorted_s)

            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
            
        return list(ans.values())
