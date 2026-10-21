class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        groups = dict()
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word not in groups: # match as anagram:
                groups[s_word] = [word]
                # add to existing value
            else:
                #return a new value group
                groups[s_word].append(word)
        # return the lists of the anagrams, each one being an entry in the dictionary
        return list(groups.values())
