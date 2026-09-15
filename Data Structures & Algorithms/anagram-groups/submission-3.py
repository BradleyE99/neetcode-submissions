class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()

        # keys: the anagram in alphebetical order
        # values: each word

        for i, s in enumerate(strs):
            curr_s = "".join(sorted(s))
            
            if curr_s not in store:
                store[curr_s] = [s]
            else:
                store[curr_s].append(s)
        
        return list(store.values())
