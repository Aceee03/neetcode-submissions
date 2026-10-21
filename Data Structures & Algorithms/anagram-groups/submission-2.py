class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        tracker = {}

        for s in strs:
            s_tuple = tuple(sorted(s))

            if s_tuple in tracker:
                tracker[s_tuple].append(s)
            else:
                tracker[s_tuple] = [s]
            
        return list(tracker.values())

        
        


            
